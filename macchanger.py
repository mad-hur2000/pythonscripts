#!/usr/bin/env python3

import subprocess
import optparse
import re

def change_mac(interface , address):
    # print('[+] changing mac address of ' + interface + ' to ' + address)
    # subprocess.call('ifconfig ' + interface + ' down',shell=True)
    # subprocess.call('ifconfig ' + interface + ' hw ether ' + address ,shell=True)
    # subprocess.call('ifconfig ' + interface + ' up',shell=True)
    # secure way
    subprocess.call(['ifconfig', interface , 'down'])
    subprocess.call(['ifconfig', interface , 'hw' , 'ether', address])
    subprocess.call(['ifconfig', interface , 'up'])
    # print('mac address of ' + interface + ' changed to ' + address )

def get_arguments(): 
    parser=optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface' , help='interface to change MAC address')
    parser.add_option('-m', '--mac', dest='address' , help='new MAC address to be used')
    (options, arguments)=parser.parse_args()
    if not options.interface:
        #error msg
        parser.error('[-]please enter interface to be used. Type -h for more help')
    elif not options.address:
        #error msg
        parser.error('[-]please enter new MAC address. Type -h for more help')
    return options

def get_current_mac(interface):
    ifconfig_output=subprocess.check_output(['ifconfig',interface])
    mac_from_output=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_output)

    if mac_from_output:
        return(mac_from_output.group(0))
    else:
        print('[-] Couldn\'t read mac address')

# interface = input('give interface : ') #raw_input for python2
# address = input('specify desired address : ')

options= get_arguments()

current_mac_from_output=get_current_mac(options.interface)

print('current MAC address is ' + str(current_mac_from_output))

change_mac(options.interface,options.address)

current_mac_from_output=get_current_mac(options.interface)

if current_mac_from_output==options.address:
    print('[+] MAC changed successfully to ' + options.address)
else:
    print('[-] MAC was not changed and current MAC is ' + str(current_mac_from_output) + ' for ' + options.interface)

