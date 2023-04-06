# Hero Game for Udemy
Uno de los proyectos principales del [Curso de Desarrollo Web de Python con Django](https://www.udemy.com/course/desarrollo-de-sitios-web-con-python-3-con-django/?referralCode=A491B0944C634BFAA48C).

Se trata de un juego de rol donde creamos un personaje el cual va a poder luchar en una arena con distintos enemigos, comprando equipamiento en una tienda y mejorando sus stats.

## Apps
Este proyecto de Django se divide en varias apps, las cuales representan distintos features del juego:
- app: El módulo principal, el cual se alimenta de todo el resto.
- arena: Este módulo se integra con Characters, y contiene el sistema de batalla que permitirá enfrentar entidades.
- blog: Sistema de novedades del juego. Se combina con el sistema de autenticación y roles de usuario. Es un CRUD de artículos.
- Character: Este módulo representa al Player y el Enemy, pero está pensado para agregar cualquier tipo de entidad que pueda interactuar con la Arena o la tienda.
- Shop: Tienda del juego, donde un Character que posea inventario y dinero puede comprar y equiparse armas.

## API
En el módulo app podemos encontrar un archivo [api.py](app/api.py), el cual contiene los métodos que exponen una API del CRUD de la entidad Player.
Por otro lado, también se incluyen métodos para autenticar usuarios.

## Instalación
Primero debemos instalar los paquetes de npm:
> npm install

Luego, con un entorno de python creado:
> pip install -r requirements.txt

El cual descargará las librerías utilizadas por django.
Finalmente para correr el proyecto utilizaremos:
> python manage.py runserver