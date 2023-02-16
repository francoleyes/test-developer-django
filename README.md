# DJANGO - API - WEBSCRAPING
Proyecto de django que incluye WebScraping y extracción de datos mediante API.
Test Práctico.

## Instrucciones de Ejecución

- Clonar el repositorio: git clone https://github.com/francoleyes/test-developer-django.git
- Acceder a la carpeta del proyecto: cd bike-santiago
- Instalar las dependencias: pip install -r requirements.txt
- Crear base de datos en postgresql y completar nombre, usuario y password en settings.py
- Realizar las migraciones de la base de datos: python manage.py migrate
- Ejecutar el servidor: python manage.py runserver
- Acceder a la dirección http://localhost:8000/

## Descripción primer tarea

Se ha desarrollado una aplicación web en Django que consulta una API pública de bicicletas en Santiago de Chile, almacena los datos obtenidos en una base de datos y los muestra en una tabla paginada en una página web utilizando Bootstrap.
Se utiliza el modelo BikeSantiago para almacenar la información obtenida de la API, que se obtiene a través de una función en views.py.
La vista bike_santiago_view es la encargada de manejar la petición GET y mostrar la tabla paginada en la página web, utilizando la plantilla bikesantiago.html.
En cuanto a la estructura del proyecto, se han creado las carpetas y archivos necesarios siguiendo la convención de nombres de Django. En la carpeta core se han creado las plantillas, el archivo urls.py y los archivos views.py y models.py. También se han agregado las configuraciones de la base de datos y de la aplicación en el archivo settings.py.

## Descripción segunda tarea 

En este último desarrollo se completó la tarea de crear un script llamado 'scraper.py' (que se puede encontrar en 'core') que obtiene la información presentada en una tabla en una página web y la guarda en un archivo JSON.
Además, se creó una vista en el administrador de Django para visualizar la información obtenida, y se creó una vista con Bootstrap 5 para mostrar la información en una tabla en el sitio web.
Finalmente, se agregó una función para cargar los datos desde el archivo JSON al modelo de Django. 
