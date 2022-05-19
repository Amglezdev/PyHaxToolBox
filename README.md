# PyHaxToolBox


[PyHaxToolBox](https://github.com/Amglezdev/PyHaxToolBox) es un proyecto escrito en Python orientado a ciberseguridad consiste en una pequeña colección de programas que cumplen distintas funciones, podríamos verlo como una cajita de herramientas.

Pequeño disclaimer, estas herramientas están pensadas para ser usadas en “ethical hacking”, no nos responsabilizamos de cualquier mal uso de estas.

Dependencias : [pip](https://pip.pypa.io/en/stable/installation/), [urrlib](https://pypi.org/project/urllib3/), [paramiko](https://www.paramiko.org/installing.html), [socket](https://pypi.org/project/sockets/), [socketserver](https://pypi.org/project/systemd-socketserver/)

## [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py)

El primero que vamos a ver es el [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py), como su nombre indica es una herramienta la cual escanea un servidor buscando que puertos están abiertos en ese momento.

Un problema que hemos encontrado es que es tiende a tomarse entre 2 y 3 minutos analizando los puertos mas comunes, pero si queremos analizar en el rango entre el 1 y el 3000, vamos a tardar bastante por el tiempo que tardan los servidores en mandar la respuesta.

Principalmente se usan sockets para establecer la conexión con el host, además, nos guardara en un fichero de texto las ip´s que hayamos analizado y los puertos que tienen abiertos.

## [phWordPressFinder](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phWordpressFinder.py)

[phWordPressFinder](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phWordpressFinder.py) es una herramienta que podemos utilizar para averiguar que servidores usan [Wordpress](https://es.wikipedia.org/wiki/WordPress) para ofrecer sus servicios, la forma en la que hace esto es usando un request del código html del archivo wp-login que tienen todos los Wordpress.

Esto puede ser muy útil ya que las versiones antiguas de Wordpress tienen varias vulnerabilidades y sabiendo que servidores lo utilizan, podemos llegar a conseguir acceso a estos.

## [phBruteForce](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phBruteForce.py)

### Importante!! Antes de usar este script es muy recomendable usar [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py) para saber si el [SSH](https://es.wikipedia.org/wiki/Secure_Shell) está en el puerto 22, ya que por defecto atacaremos a este.

En este programa va a requerir una wordlist para funcionar correctamente, por defecto, vamos a utilizar un fichero de texto con unas contraseñas de ejemplo, pero lo recomendable es buscar alguna para su garantizar su correcto funcionamiento. Para cambiarlo simplemente tendríamos que cambiar el nombre del fichero del que leemos.

Para realizar el intento de inicio de sesión, vamos a utilizar la librería paramiko (para poder instalar esta librería usaremos la herramienta [pip](https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes))).

Una vez encuentre unos credenciales que funcionen en el servidor, nos los mostrará para que hagamos lo que veamos propio con esa información.
