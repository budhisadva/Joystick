# Joystick

Para ejecutar este proyecto debes:

Tener instalado Python 3, Thonny, tu placa conectada correctamente.

## Pi Pico

El archivo "main.py" dentro de la carpeta embebido/ tiene el codigo
que debes subir a tu placa por medio de Thonny.

## Servidor Django

1. Crear una maquina virtual
  $ python3 -m venv <nombre>
  $ source <nombre>/bin/activate

2. Instalar las dependecias dentro de requirements.txt
  $ pip install -r requirements.txt

3. Lanzar el servidor:
  $ python manage.py runserver

4. Ingresar desde el navegador
  http://localhost:8000/juego/

Para la configuracion del puerto, revisar archivo Interfaz/juego/consumers.py
