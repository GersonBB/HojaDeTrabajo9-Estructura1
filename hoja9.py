import os
import networkx as nx
import matplotlib.pyplot as plt

def construir_grafo(archivo):
    G = nx.Graph()
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            origen, destino, costo = linea.strip().split(',')
            origen = origen.strip().strip('"')
            destino = destino.strip().strip('"')
            G.add_edge(origen, destino, weight=int(costo.strip()))
            G.add_edge(destino, origen, weight=int(costo.strip()))  # Rutas simétricas
    return G

def mostrar_destinos_disponibles(grafo, estacion_salida):
    print(f"Destinos disponibles desde {estacion_salida}:")
    for vecino in grafo.neighbors(estacion_salida):
        print(f"- {vecino}")

def dijkstra(grafo, estacion_salida):
    return nx.single_source_dijkstra_path(grafo, estacion_salida)

def desplegar_grafo(grafo):
    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(grafo)  # O cambia a otra disposición que prefieras
    nx.draw(grafo, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray', width=2)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.title("Grafo de Rutas", fontsize=16, fontweight='bold')  # Agregar título al grafo
    plt.show()

def main():
    # Obtenemos la ruta del directorio donde se encuentra el script
    directorio_actual = os.path.dirname(__file__)
    # Concatenamos el nombre del archivo al directorio para obtener la ruta completa
    archivo = os.path.join(directorio_actual, 'archivo.txt')

    grafo = construir_grafo(archivo)

    while True:
        print("\n----- Menú -----")
        print("1. Ver destinos disponibles desde una estación de salida")
        print("2. Encontrar la ruta más corta usando Dijkstra")
        print("3. Desplegar grafo de destinos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            estacion_salida = input("Ingrese la estación de salida: ").strip()
            if estacion_salida in grafo:
                mostrar_destinos_disponibles(grafo, estacion_salida)
            else:
                print("La estación de salida ingresada no existe en el grafo.")
        elif opcion == '2':
            estacion_salida = input("Ingrese la estación de salida: ").strip()
            if estacion_salida in grafo:
                rutas_cortas = dijkstra(grafo, estacion_salida)
                print("Rutas más cortas desde", estacion_salida)
                for destino, ruta in rutas_cortas.items():
                    print(destino, "->", ruta)
            else:
                print("La estación de salida ingresada no existe en el grafo.")
        elif opcion == '3':
            desplegar_grafo(grafo)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

