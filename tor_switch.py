#!/bin/python3

#--------------------------------------------------------------------------#

#  tor node switching  script switches tor nodes in every interval of time

#  --- A simple script created by -- d4rk sh4d0w 
 
#  -- Script only works on linux not in windows operating system

# --- Hello to s0u1 :) 
#-------------------------------------------------------------------------#

import os
try:
	import os

except:
	print("[!] You need to install os module [!] ")	

import time
import pyfiglet
from colorama import Fore , Style
import sys

if (sys.platform == "win32") or (sys.platform == "win64"):
	print(" [!] This script cannot be used in the windows it is used in linux [!] ")
	sys.exit()

fancy_banner = pyfiglet.figlet_format("   TOR   SWITCHER  " ) 
os.system("clear")

print(Fore.BLUE , fancy_banner)
print(Style.RESET_ALL)
print(Fore.RED , "\t\t[+] SCRIPT CODED BY  ->> d4rk sh4d0w [+]\n\n\t[+] Follow d4rk sh4d0w at Github ->> https://github.com/d4rkconsole [+] ")
print(Style.RESET_ALL)
print(Fore.GREEN , "-" * 90)

print("\n")
interval = int(input(" [+] Enter time of interval before switching  ->> "))
try:
	os.system("sudo service tor start")
except:
	print(Fore.BLUE , " [!] Tor Service Not installed You need to install it [!] ")
	print(Fore.BLUE , "[+] Install tor service in Linux using command - sudo apt install tor -y ")
print("-" * 90)
print(Style.RESET_ALL)

try:

	while True:
	
		print(Fore.BLUE , "\n[+] Ip Address changed , Sleeping For {} Seconds before switching .... " .format(interval))
		time.sleep(interval)
		os.system(" sudo service tor restart ")
except KeyboardInterrupt:

	print(Fore.RED , "\n[+] Stopping tor service ...")
	print(Style.RESET_ALL)
	os.system("sudo service tor stop")
	print(Fore.RED , "[+] Tor service stopped sucessfully ... ")




	


	
	





