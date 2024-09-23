import charts

def run():
    # Definir etiquetas y valores
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    
    # Llamar a la función para generar el gráfico
    charts.generate_pie_chart(labels, values, filename='mi_pie_chart.png')

if __name__ == '__main__':
    run()
