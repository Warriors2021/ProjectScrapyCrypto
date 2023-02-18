from selenium import webdriver  # Importa la biblioteca de Selenium para Python
from selenium.webdriver.common.by import By  # Importa la clase "By" para buscar elementos en la página
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Importa la clase "EdgeChromiumDriverManager" para manejar la descarga e instalación del controlador de Microsoft Edge
from selenium.webdriver.edge.options import Options

# Crea las opciones del controlador de Edge
edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument('--headless')
edge_options.page_load_strategy = 'normal'

def ScrapyBinance():  # Define la función "ScrapyBinance"
    lista = []  # Inicializa una lista vacía para almacenar los datos extraídos
    for pagina in range(1,3):  # Ciclo for que recorre las páginas de la web de Binance de la página 1 a la página 2
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(),options=edge_options)  # Crea una instancia del controlador de Microsoft Edge y especifica la ubicación del controlador utilizando EdgeChromiumDriverManager().install()
        driver.get(f"https://www.binance.com/es/markets?p={pagina}")  # Utiliza el método "get()" del controlador para cargar la página web de Binance para la página actual
        for x in driver.find_elements(By.CSS_SELECTOR, "div.css-vlibs4"):  # Utiliza el método "find_elements()" del controlador para buscar todos los elementos en la página web que coinciden con el selector CSS "div.css-vlibs4"
            diccionario = {  # Crea un diccionario con dos claves, "text" y "price", que se agregarán a la lista "lista"
                "Cripto": x.find_element(By.CSS_SELECTOR, "div.css-1x8dg53").text,  # Utiliza el método "find_element()" del objeto "x" para encontrar el elemento que contiene el nombre del producto y obtener su texto
                "Price": x.find_element(By.CSS_SELECTOR, "div.css-ydcgk2 > div").text  # Utiliza el método "find_element()" del objeto "x" para encontrar el elemento que contiene el precio del producto y obtener su texto
            }
            lista.append(diccionario)  # Agrega el diccionario a la lista "lista"
        driver.quit()  # Cierra el controlador utilizando el método "quit()"
    return lista  # Devuelve la lista completa de diccionarios que contienen los datos extraídos

"""
este código utiliza la biblioteca Selenium para extraer
los nombres y precios de los productos en la página web
de Binance para varias páginas y devuelve los datos en
una lista de diccionarios.
"""