<h1>Extracción de datos de Binance y carga en MongoDB</h1>

<p>Este código utiliza la biblioteca Selenium para extraer los nombres y precios de los productos en la página web de Binance para varias páginas y los almacena en una base de datos MongoDB.</p>

<h2>Funcionamiento del código</h2>

<p>El código consta de dos partes: la primera parte utiliza la biblioteca Selenium para extraer los datos de la página web de Binance, mientras que la segunda parte utiliza la biblioteca PyMongo para almacenar los datos en una base de datos MongoDB.</p>

<h3>Extracción de datos de Binance</h3>

<p>El código utiliza la biblioteca Selenium para extraer los nombres y precios de los productos en la página web de Binance para varias páginas. La extracción se realiza utilizando el método "find_elements()" del controlador de Selenium para buscar todos los elementos en la página web que coinciden con el selector CSS "div.css-vlibs4". Para cada elemento encontrado, se extraen el nombre y el precio del producto utilizando el método "find_element()" del objeto "x". Los datos extraídos se almacenan en una lista de diccionarios.</p>

<h3>Carga de datos en MongoDB</h3>

<p>El código utiliza la biblioteca PyMongo para almacenar los datos extraídos en una base de datos MongoDB. La clase "conexion_mongo" se encarga de la conexión y manipulación de la base de datos. En el constructor de la clase, se crea una instancia de MongoClient utilizando el valor proporcionado para el parámetro "host", se accede a la base de datos especificada en el parámetro "db" y se guarda una referencia a esta base de datos en el atributo "db" de la clase, se guarda el nombre de la base de datos especificada en el parámetro "db" en el atributo "nombre_database" de la clase, se guarda una referencia a la colección especificada en el parámetro "coleccion" en el atributo "coleccion" de la clase y se guarda el nombre de la colección que se pasa por parámetro al constructor en el atributo "nameCollection" de la clase.</p>

<p>La función "SubirDatosMongo()" se encarga de subir los datos extraídos por la función "ScrapyBinance()" a la colección guardada en el atributo "coleccion". La función "EliminarCollection()" se encarga de eliminar la colección guardada en el atributo "coleccion" de la base de datos.</p>

<h2>Requerimientos</h2>

<ul>
	<li>Python 3.x</li>
	<li>Las bibliotecas de Python especificadas en el archivo "requirements.txt": Selenium, webdriver_manager, pymongo, scrapy</li>
	<li>Un controlador compatible con el navegador Microsoft Edge (para Selenium)</li>
	<li>Una instancia de MongoDB en ejecución</li>
</ul>


