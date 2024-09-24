import requests

def get_categories():
    try:
        r = requests.get('https://api.escuelajs.co/api/v1/categories', timeout=10)
        r.raise_for_status()  # Verifica si hubo algún error en la respuesta
        
        # Procesar respuesta
        categories = r.json()  # Parsear JSON solo una vez
        for category in categories:
            print(category.get('name', 'No Name'))  # Obtener 'name' de manera más segura

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Manejo de errores HTTP
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")  # Manejo de cualquier otro error relacionado con requests
    finally:
        print("Finalizó la solicitud")
