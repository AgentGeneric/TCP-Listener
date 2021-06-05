import socket
import bcolors
import time
import sys

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(' ')


try:
    IpInput = input(f"{bcolors.WARNING}[-] IP To Listen On: ")
    portInput = int(input(f"{bcolors.WARNING}[-] Port To Listen On: "))

    try:
        socketObject.bind((IpInput, portInput))
        print(bcolors.OK + "[+] Started Listener on " + IpInput, ':' ,portInput)
        print(' ')
        print(bcolors.WARNING + "[+] Listening For Connections...")

    except:
        print(bcolors.FAIL + "[!] Invalid Port Number Or IP Address !")
        exit()

    socketObject.listen(1)

    def startListener():
        while True:
            targetRecieve, targetIPAddress = socketObject.accept()       
            print(' ')
            print(bcolors.OK + "[+] Connection Recieved from", str(targetIPAddress))
    startListener()

except KeyboardInterrupt:
    sys.exit()
