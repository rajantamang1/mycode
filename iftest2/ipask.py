#!/usr/bin/env python3
import ipaddress
ipchk = input("Apply an IP address: ") # this line now prompts the user for input
try:
    ipaddress.ip_address(ipchk)



# if user set IP of gateway
    if ipchk=="192.168.2.01":
        print("Looks like the IP address is IPv4:"+ ipchk)
    elif ipchk=="2001:0db8:0a0b:12f0:0000:0000:0000:000": # if any data is provided, this will test true
    
        print("Looks like the IP address is IPv6:" + ipchk) # indented under if 
except:  # if data is NOT provided 
    print("You did not provide valid input.") #indented under else
