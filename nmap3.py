import os
import nmap3
import sys
import socket


class select:
    
    availablenmap = nmap3.Nmap()
    availablenmap3 = nmap3.NmapScanTechniques()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

if(os.name=='nt'):
    os.system('cls')
else:
    os.system('clear')

print(color.GREEN+"""

                                      d8888b.                      
                                          `88                      
88d888b. 88d8b.d8b. .d8888b. 88d888b.  aaad8'"""+color.RED+"""    88d888b. dP    dP """+color.END+"""
88'  `88 88'`88'`88 88'  `88 88'  `88     `88"""+color.RED+"""    88'  `88 88    88 """+color.END+"""
88    88 88  88  88 88.  .88 88.  .88     .88"""+color.RED+""" dP 88.  .88 88.  .88"""+color.END+"""
dP    dP dP  dP  dP `88888P8 88Y888P' d88888P"""+color.RED+""" 88 88Y888P' `8888P88 """+color.END+"""
                             88              """+color.RED+"""    88            .88 """+color.END+"""
                             dP              """+color.RED+"""    dP        d8888P"""+color.END+"""
"""
)

host = input(color.RED+"Enter ip/domain: "+color.END) 
ip = socket.gethostbyname(host)



def nmap_version_details():    
    return select.availablenmap.nmap_version()
    
def top_port_scan():    
    return select.availablenmap.scan_top_ports(host)
    
def get_subdomains():    
    return select.availablenmap.nmap_dns_brute_script(host)

def list_scan():    
    return select.availablenmap.nmap_list_scan(host)

def os_detection():    
    return select.availablenmap.nmap_os_detection(host)

def subnet_scan():    
    return select.availablenmap.nmap_subnet_scan(host)

def version_detection():    
    return select.availablenmap.nmap_version_detection(host)

#-----------

def fin_scan():    
    return select.availablenmap3.nmap_fin_scan(ip)

def idle_scan():    
    return select.availablenmap3.nmap_idle_scan(ip)

def ping_scan():    
    return select.availablenmap3.nmap_ping_scan(ip)

def syn_scan():    
    return select.availablenmap3.nmap_syn_scan(ip)

def tcp_scan():    
    return select.availablenmap3.nmap_tcp_scan(ip)

def udp_scan():    
    return select.availablenmap3.nmap_udp_scan(ip)

print(color.RED+"""
Nmap commands available\t\t\t\t\t\t Nmap Scanning Techniques"""+color.END+

color.GREEN+"""
[1] [*]"""+color.END+""" Get nmap version details\t\t\t\t """+color.GREEN+"""[8]  [*]"""+color.END+""" Nmap fin Scan"""+color.GREEN+"""
[2] [*]"""+color.END+""" Nmap top port scan\t\t\t\t\t """+color.GREEN+"""[9]  [*]"""+color.END+""" Nmap idle Scan"""+color.GREEN+"""
[3] [*]"""+color.END+""" Nmap Dns-brute-script(to get subdomains)\t\t """+color.GREEN+"""[10] [*]"""+color.END+""" Nmap ping Scan"""+color.GREEN+"""
[4] [*]"""+color.END+""" Nmap list scan\t\t\t\t\t\t """+color.GREEN+"""[11] [*]"""+color.END+""" Nmap syn Scan"""+color.GREEN+"""
[5] [*]"""+color.END+""" Nmap Os detection\t\t\t\t\t """+color.GREEN+"""[12] [*]"""+color.END+""" Nmap tcp Scan"""+color.GREEN+"""
[6] [*]"""+color.END+""" Nmap subnet scan\t\t\t\t\t """+color.GREEN+"""[13] [*]"""+color.END+""" Nmap udp Scan"""+color.GREEN+"""
[7] [*]"""+color.END+""" Nmap version detection\t\t\t\t\t """+color.GREEN+"""[14] [*]"""+color.RED+""" Exit 
"""
)

option = input(color.RED+"Enter options: "+color.END)

if(option==1):
    print("Get nmap version details..")
    print(nmap_version_details())

elif(option==2):
    print("Nmap top port scan \n")
    print(top_port_scan())


elif(option==3):
    print("Nmap Dns-brute-script(to get subdomains) \n")
    print(get_subdomains())


elif(option==4):
    print("Nmap list scan \n")
    print(list_scan())


elif(option==5):
    print("Nmap Os detection \n")
    print(os_detection())


elif(option==6):
    print("Nmap subnet scan \n")
    print(subnet_scan())


elif(option==7):
    print("Nmap version detection \n")
    print(version_detection())

elif(option==8):
    print("Nmap fin Scan \n")
    print(fin_scan())

elif(option==9):
    print("Nmap idle Scan \n")
    print(idle_scan())


elif(option==10):
    print("Nmap ping Scan \n")
    print(ping_scan())


elif(option==11):
    print("Nmap syn Scan \n")
    print(syn_scan())


elif(option==12):
    print("Nmap tcp Scan \n")
    print(tcp_scan())


elif(option==13):
    print("Nmap udp Scan \n")
    print(udp_scan())

elif(option==14):
    print("çıkış..")
    sys.exit()

else:
    print("Error option")






