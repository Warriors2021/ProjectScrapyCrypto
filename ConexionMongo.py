# Importar la clase MongoClient desde el módulo pymongo
from pymongo import MongoClient

# Importar la clase ScrapyBinance desde el módulo scrapy
from scrapy import ScrapyBinance


# Definir la clase "conexion_mongo"
class conexion_mongo:

    # Constructor de la clase
    def __init__(self, host: str = 'localhost', db: str = 'DbTest', coleccion: str = "ColeccionTest"):
        # Crear una instancia de MongoClient utilizando el valor proporcionado para el parámetro "host"
        self.host = MongoClient(host)

        # Acceder a la base de datos especificada en el parámetro "db" y guardar una referencia a esta base de datos en el atributo "db" de la clase
        self.db = self.host[db]

        # Guardar el nombre de la base de datos especificada en el parámetro "db" en el atributo "nombre_database" de la clase
        self.nombre_database = db

        # Guardar una referencia a la colección especificada en el parámetro "coleccion" en el atributo "coleccion" de la clase
        self.coleccion = self.db[coleccion]

        #Guarda el nombre de la coleccion que se pasa por parametro al constructor
        self.nameCollection = coleccion

    # Función que devuelve la referencia a la colección guardada en el atributo "coleccion"
    def mi_coleccion(self):
        return self.coleccion

    # Función que devuelve una lista de los nombres de todas las colecciones en la base de datos guardada en el atributo "db"
    def List_colecciones(self):
        return self.db.list_collection_names()

    # Función para subir datos a MongoDB
    def SubirDatosMongo(self):
        # Ejecuta y guarda los datos que retorna la funcion ScrapyBinance
        datos = ScrapyBinance()

        # Insertar los datos extraídos por la funcion  ScrapyBinance en la colección guardada en el atributo "coleccion"
        self.coleccion.insert_many(datos)

    #Funcion para eliminar una coleccion
    def EliminarCollection(self):

        #Elimina una coleccion de la base de datos
        self.db.drop_collection(self.nameCollection)
