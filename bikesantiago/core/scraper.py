import requests
from bs4 import BeautifulSoup
import json

# Definimos la URL base y la página inicial
base_url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
page = 1

# Definimos una lista para almacenar los datos de la tabla
proyectos = []

# Limitación de páginas para el web scraping para que no tarde demasiado (poner -1 si se necesitan correr todas)
limite_de_paginas = 10

while True:
    # Construimos la URL con el número de página
    url = f"{base_url}?_paginador_fila_actual={page}"
    
    # Obtenemos el contenido de la página
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "tabla_datos"})

    # Salimos del bucle si no hay más páginas
    if not table:
        break

    # Recorremos los datos de la tabla y los añadimos a la lista
    for row in table.find_all("tr")[1:]:
        data = row.find_all('td')
        if len(data) >= 2:
            numero = data[0].text.strip()
            nombre = data[1].text.strip()
            tipo = data[2].text.strip()
            region = data[3].text.strip()
            tipologia = data[4].text.strip()
            titular = data[5].text.strip()
            inversion = data[6].text.strip()
            fecha_presentacion = data[7].text.strip()
            estado = data[8].text.strip()

            # Añadimos los datos a la lista
            proyectos.append({
                "num": numero,
                "name": nombre,
                "type": tipo,
                "region": region,
                "typology": tipologia,
                "holder": titular,
                "investment": inversion,
                "date_presentation": fecha_presentacion,
                "state": estado
            })

    # Aumentamos el número de página para la próxima iteración
    page += 1

    if page == limite_de_paginas:
        break

# Convertimos los datos a formato JSON y los guardamos en un archivo
with open("proyectos.json", "w") as file:
    json.dump(proyectos, file)
