#!/usr/bin/env python3
import ipaddress
ipchk = input("Apply an IP address: ") # this line now prompts the user for input
ipv6 = "2001:0db8:0a0b:12f0:0000:0000:0000:0001"
ipv4 = "192.168.2.10"

# if user set IP of gateway
if ipaddress.IPv4Address(ipchk):
    print("Looks like the IP address is IPv4:"+ ipchk)
elif iaddress.IPv6Address(ipchk): # if any data is provided, this will test true
    print("Looks like the IP address is IPv6:" + ipchk) # indented under if 
else:  # if data is NOT provided 
    print("You did not provide input.") #indented under else
