import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_numbers():
    """
    Ruta principal que devuelve una lista de números.
    """
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def contact_page():
    """
    Ruta que devuelve una página HTML con un título y un párrafo.
    """
    return """
        <h1>Hola, soy una página</h1>
        <p>Soy un párrafo de ejemplo.</p>
    """

def fetch_categories():
    """
    Llama a la API de categorías desde el módulo 'store'.
    """
 
    store.get_categories()
 

if __name__ == '__main__':
    fetch_categories()
