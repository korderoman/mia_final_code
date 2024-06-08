import networkx as nx


class GraphDfs(object):
    def __init__(self, G):
        self.G = G

    # Función para encontrar la ruta DFS entre dos nodos
    def dfs_path(self, graph, start, goal):
        # Genera un árbol DFS desde el nodo de inicio
        dfs_tree = nx.dfs_tree(graph, source=start)
        # Intentar encontrar un camino al nodo objetivo
        try:
            path = nx.shortest_path(dfs_tree, source=start, target=goal)
            return path
        except nx.NetworkXNoPath:
            return None

    def getRoute(self, church_nodes):
        # Implementar DFS para recorrer las iglesias
        route = []
        current_node = church_nodes[0]
        for next_node in church_nodes[1:]:
            path = self.dfs_path(self.G, current_node, next_node)
            if path:
                route.extend(path[:-1])  # Evitar duplicar nodos
            current_node = next_node

        # Agregar el último segmento para cerrar el ciclo
        route.append(current_node)
        return route