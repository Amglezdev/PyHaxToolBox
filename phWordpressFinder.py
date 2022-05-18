import urllib.request
import urllib



def site_checker():
    sites = open("wpCheckList.txt", 'r')
    line = sites.readlines()

    for li in line:
        url = urllib.request.urlopen(li + "/wordpress/wp-login.php")
        print(url)
        data = url.read()
        line = sites.readlines()
        print(data)
        break

    

site_checker()





