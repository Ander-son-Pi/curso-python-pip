import store

def run():
    #Llama a la funcion que solicita un GET a una api
    store.get_categories()
    
if __name__ == '__main__':
    run()