import urllib.request
import urllib
#@Author amglezdev



#This one just checks if a specefic host has a wordpress site
def site_checker():
    sites = open("wpCheckList.txt", 'r') #We just give it a list of hosts and wait for him to do his thing
    line = sites.readlines()

    for li in line:
        url = urllib.request.urlopen(li + "/wordpress/wp-login.php")
        print(url)
        data = url.read()
        line = sites.readlines()
        print(data)
        break

    

site_checker()





