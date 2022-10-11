#This program is a fast way to automatically save our progress in github or whatever other git repository we use
#it uses os library to execute the proper commands


#@Author amglezdev

import os

def auto_add() : #Automatically adds all files to our repository
    os.system("git add .")
    return True

def auto_commit(): #Automatically commits all changes to our local rpository
    os.system("git commit -m  \"#Automatic commit by @phAutoGit\"")    
    return True

def auto_push(): #Automatically pushes all changes to github repository
    os.system("git push origin master")
    return True

#The way we are going to execute this, is by checking if the previous process was done

if(auto_add() is True):
    if(auto_commit() is True):
        auto_push()