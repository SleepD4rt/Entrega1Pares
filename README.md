# Entrega1Pares

Desarrollado en Windows 10.

Proyecto entregable para CODERHOUSE, actividad "Entrega intermedia de tu proyecto Final".
En Git bash o bash
Realizar un:
```bash
git clone https://github.com/SleepD4rt/Entrega1Pares.git
```
Ya cuenta con una base de datos para mostrar su contenido. 

Entrar en el directorio del proyecto.

```bash
cd Entrega1Pares
```
En bash tipear para entrar en el IDE de VisualStudioCode.

```bash
code .
```

En el VSC tipear en el terminal para crear el ambiente de desarrollo "venv".
Copiar y pegar/Escribir y ejecutar por linea.
```bash
python -m venv venv

venv/Scrips/activate
```
Teniendo en funcionamiento el entorno venv.
instalar los requerimientos para ejecutar el proyecto:
```bash
pip install -r requirements.txt
```


crear un super usuario en caso de querer explorar la url de admin:
```bash
python manage.py createsuperuser
```

Escribir si se quiere un nombre de usuario, puede darle Enter, es opcional introducir un nombre de usuario. Lo mismo para el email.
Contraseña una sencilla como para probarlo. si es sencilla le va a salir un cartel de advertencia ignorelo tipeando "y" y pulse Enter.

ejecutar el servidor:

```bash
python manage.py runserver
```

