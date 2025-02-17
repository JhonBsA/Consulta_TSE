import requests

API_URL = "http://127.0.0.1:8000/tse/consulta/"

def consultar_cedula(cedula):
    try:
        #Consulta a la API
        response = requests.get(f"{API_URL}?cedula={cedula}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None