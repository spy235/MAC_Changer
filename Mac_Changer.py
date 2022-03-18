#/usr/bin/env python3
import optparse
import re
import subprocess

#aurgements for interface and can be read from command-line in terminal
def get_args():
# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

#create a praser object to read input form the command-line aurguments
    praser = optparse.OptionParser()
    praser.add_option("-i", "--interface", dest="interface", help="Inerface to change mac address")
    praser.add_option("-m", "--mac", dest="new_mac", help=" mac address")

    (options,arguments) = praser.parse_args()#praser options take interface and mac addresses values

#to check whether a options variables contains value or not same goes to mac addresses
    if not options.interface:
        praser.error("[-] Please Specify Correct Interface")
    elif not options.new_mac:
        praser.error("[-] Please specify correct Mac Address")
    return options
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

def mac_changer(interface,new_mac):
#mac Changer funtions using subprocess module to execute system commands

    subprocess.call(["ifconfig", interface ,"down"])
    subprocess.call(["ifconfig", interface ,"hw","ether",new_mac])
    subprocess.call(['ifconfig', interface ,'up'])

def mac_dis(interface):
    # Checking The output and printing output of a command
    get_result = subprocess.check_output(["ifconfig", interface])

    print(get_result)
    result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(get_result))

    if result:
        return result.group(0)
    else:
        print("[+] No Pattern Maching")


options = get_args()
mac_changer(options.interface,options.new_mac)#passing Interface and Macaddresses as parameters
curr_mac = mac_dis(options.interface)
if curr_mac==options.new_mac:
    print("[+] Mac Has Been Changed >>> "+curr_mac)
else:
    print("[-] Mac Has Not Changed")


