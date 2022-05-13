import urllib.request
import urllib



def site_checker():
    sites = open("wpCheckList.txt", 'r')
    line = sites.readlines()

    for li in line:
        url = urllib.request.urlopen(li + "/wp-login")
        data = url.read()
        print(data)
        break



