# Importamos el módulo personalizado 'ConexionMongo' que contiene la lógica para conectarnos y operar con una base de datos MongoDB
from ConexionMongo import conexion_mongo

# Importamos el módulo 'time' para poder hacer una pausa en el bucle
import time

# Importamos el módulo 'datetime' para obtener la fecha y hora actual
from datetime import datetime

# Definimos la función 'conteo_regresivo(n)' que hace un conteo regresivo durante 'n' segundos
def conteo_regresivo(n):

    z = n - 1

    # Hacemos un bucle anidado que cuenta desde 'n' hasta 1, y luego desde 60 hasta 0
    for i in range(n, 0, -1):
        for y in range(60,0,-1):

            # Imprimimos el tiempo restante en cada iteración del bucle
            if y < 11:
                print(f"Tiempo restante, {z}:0{y-1} MINUTOS")
            else:
                print(f"Tiempo restante, {z}:{y-1} MINUTOS")

            # Hacemos que el programa espere un segundo antes de imprimir el siguiente número
            time.sleep(1)

        z = z - 1

    # Imprimimos un mensaje final cuando el conteo regresivo ha terminado
    print("¡Tiempo finalizado!")

# Iniciamos un bucle infinito que se ejecutará continuamente
while(True):

    # Mostramos la fecha y hora actual
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

    # Llamamos a la función 'conteo_regresivo()' con un argumento de 5 minutos para iniciar el conteo regresivo
    conteo_regresivo(5)

