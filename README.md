# PyHaxToolBox


[PyHaxToolBox](https://github.com/Amglezdev/PyHaxToolBox)  is a school project about cybersecurity using python, you could look a it as if it was a little tool box for your ethical hacking.

Dependencias : [pip](https://pip.pypa.io/en/stable/installation/), [urrlib](https://pypi.org/project/urllib3/), [paramiko](https://www.paramiko.org/installing.html), [socket](https://pypi.org/project/sockets/), [socketserver](https://pypi.org/project/systemd-socketserver/), [threading](https://docs.python.org/3/library/threading.html)

## [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py) ( No threading version )

[phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py) is a port scanner which was made using the library named paramiko,

I do not recommend you use the multiple ports scan, at least on this version due to being really slow, its best to just attack the commonly opened ports

It mainly uses socket to try and connect to servers.

## [phScannerThreading](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phTrheadingScanner.py)

Since [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py) was limited to scan 1 port at a time, the best option was to create a version using threading, it is basically the same program, just faster.

## [phWordPressFinder](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phWordpressFinder.py)

[phWordPressFinder](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phWordpressFinder.py) is a tool which allows us to know which sites are made using [Wordpress](https://es.wikipedia.org/wiki/WordPress), it sends a request to get some html code from wp-login.php file.

This one in particular might come in handy in case we want to see how secure [Wordpress](https://es.wikipedia.org/wiki/WordPress)really is.

## [phBruteForce](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phBruteForce.py)

[phBruteForce](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phBruteForce.py) is a brute force script which uses a wordlist with some commonly used passwords to try and connect to servers.

Before using this script, i highly recommend using either [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py) or [phScannerThreading](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phTrheadingScanner.py) since some servers may not have SSH on port 22.

## [phAutoGit](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phAutoGit.py)

[phAutoGit](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phAutoGit.py) is a tool i developed to save some time pushing and commiting projects to github
