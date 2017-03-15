from __future__ import print_function
import os

if os.name == "posix":
    macAddress = input("Enter mac to change to:")
    if len(str(macAddress)) == 12:
        hexMac = ':'.join(str(macAddress)[i:i+2] for i in range(0, len(str(macAddress)), 2))
        print (hexMac)
        os.system("sudo -S ifconfig en0 ether "+hexMac)
""" Work is in process for other OS elif os.name == "nt":
    macAddress = input("Enter mac to change to:")
    if len(str(macAddress)) == 12:
        hexMac = ':'.join(str(macAddress)[i:i + 2] for i in range(0, len(str(macAddress)), 2))
        print(hexMac)
        os.system("" + hexMac)"""
