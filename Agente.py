import osmnx as ox
import matplotlib.pyplot as plt
from SearchGraphBFS import GraphBfs

class Agente(object):

    def descargarGrafoDistrito(self, distrito):
        # Obtener el grafo
        place_name = "$distrito, Lima, Peru"
        return ox.graph_from_place(place_name.replace("$distrito", distrito), network_type='drive')

    def descargarIglesias(self, distrito):
        # Obtener iglesias
        place_name = "$distrito, Lima, Peru"
        tags = {'amenity': 'place_of_worship', 'religion': 'christian'}  # Tags para buscar iglesias
        churches = ox.features_from_place(place_name.replace("$distrito", distrito), tags)
        return churches[churches.geometry.type == 'Point']

    def preprocesarGrafo(self, G, churches):
        church_nodes = []
        for idx, church in churches.iterrows():
            point = church.geometry
            nearest_node = ox.nearest_nodes(G, point.x, point.y)  # Usamos nearest_nodes
            church_nodes.append(nearest_node)
        return church_nodes

    def buscarMejorRuta(self, G, church_nodes):
        bfs = GraphBfs()
        print("Busqueda de la Mejor Ruta con BFS:")
        return bfs.getRoute(G, church_nodes)

    def calculate_route_length(self, G, route):
        length = 0.0
        for i in range(len(route) - 1):
            edge_data = G.get_edge_data(route[i], route[i+1])
            length += edge_data[0]['length']  # Asume que la longitud está en edge_data[0]['length']
        return length

    def visualizarGrafo(self, G, church_nodes, route):
        # Visualizar la ruta junto con las iglesias
        #fig, ax = plt.subplots(figsize=(24, 16))
        fig, ax = ox.plot_graph(G, show=False, close=False, node_color='gray', node_size=20, edge_linewidth=0.5, edge_color='#B0B0B0')
        #ox.plot_graph(self.G, ax=ax, show=False, close=False, node_color='gray', node_size=20, edge_linewidth=0.5, edge_color='#B0B0B0')

        if church_nodes is not None:
            # Dibujar las iglesias
            church_x = [G.nodes[node]['x'] for node in church_nodes if node in G.nodes]
            church_y = [G.nodes[node]['y'] for node in church_nodes if node in G.nodes]
            ax.scatter(church_x, church_y, c='red', s=100, label='Iglesias', zorder=5)

        if route is not None:
            # Dibujar la ruta manualmente
            for i in range(len(route) - 1):
                start_node = route[i]
                end_node = route[i + 1]
                start_pos = (G.nodes[start_node]['x'], G.nodes[start_node]['y'])
                end_pos = (G.nodes[end_node]['x'], G.nodes[end_node]['y'])
                ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='yellow', linewidth=3)

            # Anotar cada nodo en la ruta con su orden
            pos = 1
            for i, node in enumerate(route):
                node_point = G.nodes[node]
                if node in church_nodes:
                    #print(pos, node)
                    ax.text(node_point['x'], node_point['y'], str(pos), fontsize=6, color='white', ha='center', va='center', bbox=dict(facecolor='blue', alpha=0.5), zorder=6)
                    pos = pos + 1

        if church_nodes is not None or route is not None:
            # Asegurar que la leyenda se muestre
            ax.legend()

        # Mostrar el mapa
        plt.show()