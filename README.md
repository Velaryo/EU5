# Examen proyecto de la UNIDAD #05

## ¿Qué es Django Rest Framework?
Es un framework que nos permite el fácil desarrollo de una API REST en Python. Actualmente esta tecnología se usa en diversos proyectos.


## Pasos iniciales

- Descarga del repositorio
```bash
git clone https://github.com/Velaryo/EU5 nombre_carpeta
```

- Crear un entorno virtual en la carpeta con el repositorio descargado

```bash
virtualenv env
```

- Activar el entorno virtual

Windows

```bash
env\Scripts\activate
```

MacOS/Linux

```bash
source env/bin/activate
```

- Instalación de Django, módulos y/o librerías necesarias

```bash
pip install -r requirements.txt
```

## |-*settings.py*

```python
DATABASES = {
    'default': {
        'ENGINE': 'MOTOR de base de datos',
        'NAME': 'nombre de la DB',
        'PORT': 'puerto',
        'HOST': 'host {localhost} por defecto',
        'USER': 'usuario {root} por defecto',
        'PASSWORD': 'contraseña'
    }
}

```
#
## Autor:
- Huarca Gamero, Alvaro
#