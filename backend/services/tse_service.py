from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class TSEService:
    def __init__(self):
        # Configura el controlador de Selenium (Chrome en este caso) con Service
        service = Service(r'..\\Consulta_TSE\ChromeDriver\chromedriver.exe')
        options = Options()
        options.add_argument('--headless') # Ejecución sin abrir el navegador
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=service, options=options)

    def obtener_informacion(self, cedula):
        # Abre la página de consulta
        self.driver.get('https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx')
        
        # Espera que la página cargue completamente, esperando a que el campo de cédula esté visible
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.ID, 'txtcedula'))
        )

        # Encuentra el campo de entrada de cédula
        cedula_input = self.driver.find_element(By.ID, 'txtcedula')
        cedula_input.clear()  # Limpia el campo antes de escribir
        cedula_input.send_keys(cedula)  # Escribe la cédula

        # Encuentra y hace clic en el botón de consulta
        consultar_button = self.driver.find_element(By.ID, 'btnConsultaCedula')
        consultar_button.click()
        
        # Espera a que los resultados aparezcan en la página
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.ID, 'lblcedula'))          
        )

        # Espera a que el botón 'Mostrar Votación' esté disponible y luego hace clic
        boton_mostrar_votacion = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.ID, 'btnMostrarVotacion'))
        )
        boton_mostrar_votacion.click()

         # Espera a que la tabla de votación esté completamente cargada
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.ID, 'Gridvotacion'))
        )

        # Obtiene el HTML de la página con los resultados
        return self.driver.page_source
    
    def extraer_informacion(self, html_content):

        soup = BeautifulSoup(html_content, 'html.parser')

        try:
            # Extrae la información específica
            cedula = soup.find('span', {'id': 'lblcedula'}).text.strip()
            fecha_nacimiento = soup.find('span', {'id': 'lblfechaNacimiento'}).text.strip()
            nombre_completo = soup.find('span', {'id': 'lblnombrecompleto'}).text.strip()
            tabla_votacion = soup.find('table', {'id': 'Gridvotacion'})
            fila_datos = tabla_votacion.find_all('tr')[1] #Segunda fila contiene la provincia
            provincia = fila_datos.find_all('td')[1].text.strip()

            # Devuelve la información como un diccionario
            return {
                'cedula': cedula,
                'fecha_nacimiento': fecha_nacimiento,
                'nombre_completo': nombre_completo,
                'provincia': provincia
            }
        except AttributeError:
            return None

    #def cerrar(self):
        # Cierra el navegador
        #self.driver.quit()