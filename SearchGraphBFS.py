import networkx as nx


class GraphBfs(object):
    def __init__(self, G):
        self.G = G

    # Función para encontrar la ruta BFS entre dos nodos
    def bfs_path(self, graph, start, goal):
        # Genera un árbol BFS desde el nodo de inicio
        bfs_tree = nx.bfs_tree(graph, source=start)
        # Si el nodo objetivo es alcanzable, devuelve el camino, si no, devuelve None
        try:
            path = nx.shortest_path(bfs_tree, source=start, target=goal)
            return path
        except nx.NetworkXNoPath:
            return None

    def getRoute(self, church_nodes):
        # Implementar BFS para recorrer las iglesias
        route = []
        current_node = church_nodes[0]
        for next_node in church_nodes[1:]:
            path = self.bfs_path(self.G, current_node, next_node)
            if path:
                route.extend(path[:-1])  # Evitar duplicar nodos
            current_node = next_node

        # Agregar el último segmento para cerrar el ciclo
        route.append(current_node)
        return route