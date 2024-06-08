import networkx as nx
import math

class GraphAstar(object):
    def __init__(self, G):
        self.G = G

    def heuristic(self, u, v):
        u_x, u_y = self.G.nodes[u]['x'], self.G.nodes[u]['y']
        v_x, v_y = self.G.nodes[v]['x'], self.G.nodes[v]['y']
        return math.sqrt((v_x - u_x) ** 2 + (v_y - u_y) ** 2)

    def getRoute(self, church_nodes):
        # Suponiendo que se empieza en la primera iglesia y se planea visitar las restantes
        route = []
        current_node = church_nodes[0]
        for next_node in church_nodes[1:]:
            path = nx.astar_path(self.G, current_node, next_node, self.heuristic, weight='length')
            route.extend(path[:-1])  # Evitar duplicar nodos
            current_node = next_node

        # Agregar el último segmento para cerrar el ciclo
        route.append(current_node)
        return route