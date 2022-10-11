import socket
import socketserver
import os
import time
import queue
import threading

#@Author amglezdev
#Threading version of phScanner.py, it is much faster and efficient


#This is just to have control over what the program does
def answer(text):
    print("Do you want to " + text + "?")
    answer1 = input()
    if (answer1.lower() == 'y'):
        return True
    if (answer1.lower() == 'n'):
        return False
    while (answer1.lower() != 'n' or answer1.lower() != 'y'):
        print("The only available answers are 'y' as in yes or 'n' as in no")
        answer1 = input()
        break

#Checks if a port is open on a certain host

def threader():
    while True:
        thread = queue.get()
        



def isOpenOrNot(host, port):
    sock = socket.socket()
    try:
        timeout = time.time()
        sock.connect((host, port))
        if (timeout > 1):
            sock.close()
    except:
        # If we cannot connect, it returns false so we know it isnt open
        print("Port " + str(port) + " is not open on host " + str(host))
        return False

    else:
        # In case we were able to connect, it returns true and it will let us know it is open
        print("Port " + str(port) + " is open on host " + str(host))
        txt = open("Vulnerable.txt", "a")
        txt.write("Port " + str(port) + " is open on host " + str(host) + "\n")
        return True


#This is were we type in the data
print("Please enter host: ")
host = input()
if (answer("scan commonly open ports")):
    notSafePorts = [22, 80, 443, 500, 4500, 3036, 8080]  # In order: SSH, HTTP
    for x in notSafePorts:
        isOpenOrNot(host, x)

        #I do not recommend using this one, its really slow
        #Ill probably add threading to make it faster, just not yet
else:
    for x in range(1, 3000):
        isOpenOrNot(host, x)
