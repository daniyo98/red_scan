import socket
import os
import re

def getDevices():
        try:
            my_host_name = socket.gethostname()
            my_host_ip = socket.gethostbyname(my_host_name)
            address = socket.gethostbyaddr(my_host_ip)
            ip = address[2][0] 
            dot = 0
            ip_unicode = ''
            for letra in ip:
                if letra == '.':
                    dot = dot + 1
                    if dot >= 3:
                        ip_unicode = ip_unicode + '.'
                        break
                ip_unicode = ip_unicode + letra
            ip_unicode = str(ip_unicode)

            for i in range(255):
                os.popen('ping -w 1 -n 1 '+ip_unicode+str(i))
                print("Ping:",ip_unicode+str(i))


            f = os.popen('arp -a')
            lista_ips = []
            for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',f.read()):
                lista_ips.append(line[0])
            lista_ips_arp = []

            ##LIMPIAR IPS DE LA TABLA DE arp##
            for cont in range(len(lista_ips)):
                if str(lista_ips[cont]) == (ip_unicode+"255"):
                    break
                lista_ips_arp.append(lista_ips[cont])
            
            hostname_arp = ''
            tupla_ips_arp = ()
            lista_host_arp = []
            ##IMPORTANTE ELIMINAR DESPUES DE LAS PRUEBAS####
            lista_ips_arp.append(str(ip))#DETECTA TU PROPIA IP Y LA AÑADE A LA LISTA
            ################################################
            for e in range(len(lista_ips_arp)):
                try:
                    address_arp = socket.gethostbyaddr(str(lista_ips_arp[e]))
                    hostname_arp = address_arp[0]
                except:
                    hostname_arp = 'Unknown'
                lista_host_arp.append(hostname_arp)
            tupla_ips_arp = lista_host_arp, lista_ips_arp


            host = []
            for c in range(len(tupla_ips_arp[0])):
                lista = []
                nombre = tupla_ips_arp[0][c]
                ip = tupla_ips_arp[1][c]
                lista.append(nombre)
                lista.append(ip)
                host.append(lista)
                print(host[c])
            return host

        except:
            print("Unable to get Hostname and IP")
print("Scaning...")
list_devices = getDevices()


