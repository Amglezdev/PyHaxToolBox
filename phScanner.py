import socket
import socketserver
import os
import time


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


def isOpenOrNot(host, port):
    sock = socket.socket()
    try:
        timeout = time.time()
        sock.connect((host, port))
        if(timeout > 1):
            sock.close()



    except:
        print("Port " + str(port) + " is not open on host " + str(host))
        return False  # If we cannot connect, it returns false so we know it isnt open
    else:  # In case we were able to connect, it returns true and it will let us know it is open
        print("Port " + str(port) + " is open on host " + str(host))
        txt = open("vulnerable.txt", "a")
        txt.write("Port " + str(port) + " is open on host " + str(host))
        return True


# This two lines are just to make sure the program works properly, it install some requirements.
# os.system("sudo python setup.py install")
# os.system("pip install dnspython==2.2.1")#This allowes us to check servers using their domain name

print("Please enter host: ")
host = input()
if (answer("scan commonly open ports")):
    notSafePorts = [22,80,443,500,4500,3036,8080]
    for x in notSafePorts:
        isOpenOrNot(host, x)
else:
    for x in range(1, 3000):
        isOpenOrNot(host, x)
