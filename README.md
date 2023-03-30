# AbuseIPDB-to-Neo4j-ES
Proyecto que utiliza la API de AbuseIPDB para extraer información de IPs que hayan realizado algún tipo de ataque en los últimos 90 días, generando un archivo CSV con las IPs, las fechas de los ataques y las categorías correspondientes. Este archivo puede ser cargado posteriormente en Neo4j para generar un diagrama de grafos.
* To read the project in English go to https://github.com/gonzabaci/AbuseIPDB-to-Neo4j-EN
# Contenido
* in.txt: Archivo de texto donde se deben ingresar un máximo de 100 direcciones IP, una debajo de la otra.
* main.py: Script en Python que permite conectar con la API de AbuseIPDB.
* out.csv: Archivo de salida que contendrá los resultados de la consulta.
* requirements.txt: Archivo que contiene una lista de las dependencias necesarias para ejecutar el script.
  
# Requisitos del sistema
* Python 3
* Neo4j
* API Key de AbuseIPDB

# Instalación y uso (Windows)
Estas instrucciones proporcionan una guía para descargar y ejecutar el script de extracción de datos, así como también para cargar los resultados en Neo4j. ¡Espero que te sean útiles!

1. Clonar o descargar este repositorio.
2. Obtener una API Key de AbuseIPDB.
3. Instalar los requerimientos con "pip install -r requirements.txt".
4. Ingresar su clave API de AbuseIPDB en main.py (linea 19).
5. Ingresar las direcciones IP en el archivo in.txt. Recuerde que el máximo permitido por día por AbuseIPDB es de 100 direcciones IP.
6. Ejecute el script a través de la terminal utilizando el comando "python.exe main.py". Los resultados de la consulta se mostrarán en el archivo out.csv.
7. Descargar e instalar Neo4j desde https://neo4j.com/download/.
8. Ejecutar Neo4j y crear un nuevo proyecto. Seleccionar "New" y luego "Create project".
9. Agregar una base de datos al proyecto haciendo clic en "Add" y luego en "Local DBMS". Ingresar un nombre y contraseña para la base de datos y hacer clic en "Create".
10. Navegar a la carpeta "C:\Users\<user>\.Neo4jDesktop\relate-data\dbmss" y copiar el archivo csv "out.csv" dentro de la última base de datos creada, en la carpeta llamada "import". El path completo sería "C:\Users\<user>\.Neo4jDesktop\relate-data\dbmss\<your dbms>\import".
11. Iniciar la base de datos desde Neo4j. Hacer clic en "open" para abrir la base de datos.
12. Ejecutar el siguiente comando en la terminal de Neo4j:

```
load csv with headers from "file:///out.csv" as row
FIELDTERMINATOR ","
merge (IP:ip{ip:row.IP})
merge (CATEGORIES:categories{categories:row.CATEGORIES})
merge (IP)-[:HAS_CATEGORY {relation_date:row.DATE}]->(CATEGORIES)
```
# Ejemplo
![Grafo de ejemplo](https://i.imgur.com/hepYpGi.jpeg)

