import matplotlib.pyplot as plt

DEFAULT_COLORS = ['red', 'blue', 'green']

def generate_pie_chart(labels, values, filename='pie.png', colors=None):
    """
    Genera un gráfico circular y lo guarda como una imagen.
    
    :param labels: Lista de etiquetas para cada sección del gráfico.
    :param values: Lista de valores correspondientes a las etiquetas.
    :param filename: Nombre del archivo de imagen donde se guardará el gráfico.
    :param colors: Colores personalizados para cada sección.
    """
    if len(labels) != len(values):
        raise ValueError("Labels y values deben tener la misma longitud.")
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors or DEFAULT_COLORS[:len(labels)])
    
    try:
        plt.savefig(filename)
    except Exception as e:
        print(f"Error al guardar la imagen: {e}")
    finally:
        plt.close()
