# Importamos el módulo personalizado 'ConexionMongo' que contiene la lógica para conectarnos y operar con una base de datos MongoDB
from ConexionMongo import conexion_mongo
# Importamos el módulo 'time' para poder hacer una pausa en el bucle
import time

from datetime import datetime


# Definimos una función que imprimirá un conteo regresivo desde el número 'n' hasta 0
def conteo_regresivo(n):
    # Utilizamos un bucle 'for' para iterar desde el número 'n' hasta 0 (sin incluir el 0)
    for i in range(n, 0, -1):
        # Imprimimos el número actual en la terminal
        print(f"Tiempo restante, {i} SEGUNDOS")
        # Hacemos que el programa espere un segundo antes de imprimir el siguiente número
        time.sleep(1)
    # Imprimimos un mensaje final cuando el conteo regresivo ha terminado
    print("¡Tiempo finalizado!")





# Iniciamos un bucle infinito que se ejecutará continuamente
while(True):

    print(datetime.now())

    print("Creando conexion a base de datos.......")

    # Llamamos a la función 'conexion_mongo()' para establecer una conexión con la base de datos MongoDB
    db = conexion_mongo()
    # Llamamos al método 'EliminarCollection()' en el objeto 'db' para eliminar cualquier dato existente en la colección
    db.EliminarCollection()
    print("Actualizando datos.......")
    # Llamamos al método 'SubirDatosMongo()' en el objeto 'db' para cargar nuevos datos en la colección
    db.SubirDatosMongo()
    # Llamamos al método 'close()' en el atributo 'host' del objeto 'db' para cerrar la conexión con la base de datos
    print("Cerrando conexion con la base de datos.......")
    db.host.close()
    # Hacemos una pausa en la ejecución del programa durante 300 segundos (5 minutos)
    print("A la espera de 5 min.......")
    # Llamamos a la función 'conteo_regresivo()' con un argumento de 300 para iniciar el conteo regresivo
    conteo_regresivo(300)



