<h2>Descripción</h2>
<la>Este proyecto consiste en un programa en Python que extrae datos de la plataforma de trading Binance mediante web scraping, y los guarda en una base de datos MongoDB.</la>

<h3>El programa está compuesto por tres archivos:</h3>

<li>ScrapyBinance.py: este archivo contiene el código necesario para extraer los datos de la plataforma de trading Binance.</li>
<li>ConexionMongo.py: este archivo contiene la lógica para conectarnos y operar con una base de datos MongoDB.</li>
<li>main.py: este archivo combina los dos anteriores y se encarga de ejecutar el proceso de extracción de datos y almacenamiento en la base de datos MongoDB.</li>


<h3>Requisitos</h3>
<li>Python 3</li>
<li>Biblioteca Selenium</li>
<li>Controlador de Microsoft Edge</li>
Instalación
Descargar e instalar Python 3 desde el sitio web oficial de Python.
Instalar la biblioteca Selenium utilizando el siguiente comando de pip en la terminal: pip install selenium
Descargar e instalar el controlador de Microsoft Edge desde el sitio web oficial de Microsoft Edge o utilizando la clase EdgeChromiumDriverManager del código.
Uso
Importar el código en un archivo Python.
Llamar la función ScrapyBinance() del archivo para extraer los datos de la página web de Binance. La función devuelve una lista de diccionarios que contienen los nombres y precios de los productos en la página web.
Contribuciones
Las contribuciones son bienvenidas y pueden realizarse a través de solicitudes de extracción en GitHub.

Licencia
Este código se distribuye bajo la Licencia MIT.




__________________________________________________________________________________________________________________________________________________________
Conexión a MongoDB y extracción de datos de Binance
Este código de Python se encarga de extraer información sobre los precios y nombres de productos de Binance, una plataforma de intercambio de criptomonedas, utilizando la biblioteca Selenium. A continuación, los datos extraídos se suben a una base de datos MongoDB utilizando la biblioteca pymongo.

El código consta de dos partes principales:

ScrapyBinance(): una función que utiliza la biblioteca Selenium para extraer datos de la página web de Binance. La función recorre varias páginas de la web, buscando elementos que contienen información sobre los productos (nombre y precio) y almacenando esta información en una lista de diccionarios.

conexion_mongo: una clase que se encarga de manejar la conexión a la base de datos MongoDB y la subida de los datos extraídos por la función ScrapyBinance(). La clase contiene los siguientes métodos:

__init__(): constructor de la clase que inicializa la conexión a la base de datos y guarda referencias a la base de datos y la colección específicas.

mi_coleccion(): método que devuelve una referencia a la colección guardada en el atributo coleccion de la clase.

List_colecciones(): método que devuelve una lista de los nombres de todas las colecciones en la base de datos guardada en el atributo db de la clase.

SubirDatosMongo(): método que utiliza la función ScrapyBinance() para extraer los datos de Binance y luego los sube a la colección guardada en el atributo coleccion de la clase.

EliminarCollection(): método que elimina la colección especificada en el atributo nameCollection de la base de datos.

Requisitos previos
Python 3.x
Bibliotecas Selenium y pymongo
Controlador de Microsoft Edge
Cómo utilizar el código
Descarga o clona el código en tu computadora.
Abre el archivo conexion_mongo.py y modifica los parámetros host, db, y coleccion según tus necesidades.
Ejecuta el archivo conexion_mongo.py en la línea de comandos utilizando el comando python conexion_mongo.py. El programa ejecutará la función SubirDatosMongo() y subirá los datos extraídos por ScrapyBinance() a la base de datos MongoDB especificada.
Si deseas eliminar la colección creada, llama al método EliminarCollection() en el archivo conexion_mongo.py. Esto eliminará la colección especificada en el atributo nameCollection de la base de datos.
Notas adicionales
Si deseas extraer datos de más páginas de la web de Binance, modifica los valores de la función range() en la función ScrapyBinance().
Si deseas modificar el selector CSS utilizado para buscar los elementos en la página web, modifica los parámetros del método find_elements() en la función ScrapyBinance().
