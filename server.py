import socket
import os
import re
import scapy.all as scapy

def getDevicesScapy():
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    try:
        my_host_name = socket.gethostname()
        my_host_ip = socket.gethostbyname(my_host_name)
        address = socket.gethostbyaddr(my_host_ip)
        ip = address[2][0] #192.168.100.5
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
    except Exception as ex:
        print(ex)
        pass
    ip_add_range_entered = ip_unicode+'0/24'
    arp_result = scapy.arping(ip_add_range_entered)


def getDevices():
        try:
            my_host_name = socket.gethostname()
            my_host_ip = socket.gethostbyname(my_host_name)
            address = socket.gethostbyaddr(my_host_ip)
            ip = address[2][0] #192.168.100.5
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

            f = os.popen('arp -a')
            data = f.read()
            lista_ips = []
            for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
                lista_ips.append(line[0])
            lista_ips_arp = []

            for cont in range(len(lista_ips)):
                if str(lista_ips[cont]) == (ip_unicode+"255"):
                    break
                lista_ips_arp.append(lista_ips[cont])
            hostname_arp = ''
            tupla_ips_arp = ()

            lista_host_arp = []
            lista_ips_arp.append('192.168.100.10')

            for e in range(len(lista_ips_arp)):
                try:
                    address_arp = socket.gethostbyaddr(str(lista_ips_arp[e]))
                    hostname_arp = address_arp[0]
                except:
                    hostname_arp = 'Guest'
                lista_host_arp.append(hostname_arp)
            tupla_ips_arp = lista_host_arp, lista_ips_arp
            return tupla_ips_arp
        except:
            print("Unable to get Hostname and IP")
"""            
def getDevicesAdvance():
    try:
        my_host_name = socket.gethostname()
        my_host_ip = socket.gethostbyname(my_host_name)
        address = socket.gethostbyaddr(my_host_ip)
        ip = address[2][0] #192.168.100.5
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

        f = os.popen('arp -a')
        data = f.read()
        lista_ips = []
        for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
            lista_ips.append(line[0])
        lista_ips_arp = []
        
        for c in range(255):
            request = os.popen('ping '+ip_unicode+str(c)+' -n 1') 
            print(request.read())

        for cont in range(len(lista_ips)):
            if str(lista_ips[cont]) == (ip_unicode+"255"):
                break
            lista_ips_arp.append(lista_ips[cont])
        print(lista_ips_arp)

        lista_host_arp = []

        for e in range(len(lista_ips_arp)):
            try:
                address_arp = socket.gethostbyaddr(str(lista_ips_arp[e]))
                hostname_arp = address_arp[0]
            except:
                hostname_arp = 'Guest'
            lista_host_arp.append(hostname_arp)

        tupla_ips_arp = lista_host_arp, lista_ips_arp
        return tupla_ips_arp

    except:
        print("Unable to get Hostname and IP")
"""
list_devices = getDevices()
print("+++++++++++++MY++++++++++++++++++")
for c in range(len(list_devices[0])):
    nombre = list_devices[0][c]
    ip = list_devices[1][c]
    host = nombre +":", ip
    print(host)
print("++++++++++++++++++SCAPY++++++++++++++")
getDevicesScapy()