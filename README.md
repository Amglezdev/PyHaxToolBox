# PyHaxToolBox
Este pequeño proyecto de python orientado a ciberseguridad consiste en una pequeña colección de programas que cumplen distintas funciones, podríamos verlo como una cajita de herramientas.

## [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py)

El primero que vamos a ver es el [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py), como su nombre indica es una herramienta la cual escanea un servidor buscando que puertos están abiertos en ese momento.

Un problema que hemos encontrado es que es tiende a tomarse entre 2 y 3 minutos analizando los puertos mas comunes, pero si queremos analizar en el rango entre el 1 y el 3000, vamos a tardar bastante por el tiempo que tardan los servidores en mandar la respuesta.

Principalmente se usan sockets para establecer la conexión con el host, además, nos guardara en un fichero de texto las ips que hayamos analizado y los puertos que tienen abiertos.

## [phWordPressFinder](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phWordpressFinder.py)

[phWordPressFinder](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phWordpressFinder.py) es una herramienta que podemos utilizar para averiguar que servidores usan Wordpress para ofrecer sus servicios, la forma en la que hace esto es usando un request del código html del archivo wp-login que tienen todos los Wordpress.

Esto puede ser muy útil ya que las versiones antiguas de Wordpress tienen varias vulnerabilidades y sabiendo que servidores lo utilizan, podemos llegar a conseguir acceso a estos.

## phBruteForce

### Importante!! Antés de usar este script es muy recomendable usar [phScanner](https://github.com/Amglezdev/PyHaxToolBox/blob/master/phScanner.py) para saber si el ssh esta en el puerto 22, ya que por defecto atacaremos a este.

En este programa va a requerir una wordlist para funcionar correctamente, por defecto, vamos a utilizar un fichero de texto con una contraseña de ejemplo, pero lo recomendable es buscar alguna para su correcto funcionamiento. Para cambiarlo simplemente tendriamos que cambiar el nombre del archivo del que leemos.

```python
args = parse.parse_args()
host = "root"
passlist = args.passlist
user = args.user
```

Para realizar el intento de inicio de sesión, vamos a utilizar la libreria paramiko.
