from collections import deque, namedtuple
from geopy.distance import geodesic

A = (3.139003, 101.686852) # A for Kuala Lumpur,
B = (35.86166, 104.195396) # B for China,
C = (51.507351, -0.127758) # C for London,
D = (20.593683, 78.962883) # D for India,
E = (61.52401, 105.318756) # E for Russia,
F = (37.09024, -95.712891) # F for United States,
G = (15.870032, 100.992538) # G for Thailand,
H = (40.463669, -3.74922) # H for Spain,
I = (-14.235004, -51.925282) # I for Brazil,

distanceKL_Thailand = (geodesic(A , G ).km)
AG = round(distanceKL_Thailand, 2)
distanceKL_India = (geodesic(A , D ).km)
AD = round(distanceKL_India, 2)
distanceKL_Brazil = (geodesic(A , I ).km)
AI = round(distanceKL_Brazil, 2)
distanceThailand_China = (geodesic(G , B ).km)
GB = round(distanceThailand_China, 2)
distanceThailand_Russia = (geodesic(G , E).km)
GE = round(distanceThailand_Russia, 2)
distanceThailand_London = (geodesic(G , C ).km)
GC = round(distanceThailand_London, 2)
distanceChina_Russia = (geodesic(B , E ).km)
BE = round(distanceChina_Russia, 2)
distanceIndia_Spain = (geodesic(D , H ).km)
DH = round(distanceIndia_Spain, 2)
distanceIndia_London = (geodesic(D , C ).km)
DC = round(distanceIndia_London, 2)
distanceIndia_China = (geodesic(D , B ).km)
DB = round(distanceIndia_China, 2)
distanceIndia_Russia = (geodesic(D , E ).km)
DE = round(distanceIndia_Russia, 2)
distanceBrazil_US = (geodesic(I , F ).km)
IF = round(distanceBrazil_US, 2)
distanceBrazil_Spain = (geodesic(I , H ).km)
IH = round(distanceBrazil_Spain, 2)
distanceSpain_US = (geodesic(H , F ).km)
HF = round(distanceSpain_US, 2)
distanceSpain_London = (geodesic(F , C ).km)
FC = round(distanceSpain_London, 2)
distanceLondon_US = (geodesic(C , F).km)
CF = round(distanceLondon_US, 2)

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


graph = Graph([
    ("KL", "Thailand", AG), ("KL", "India", AD), ("KL", "Brazil", AI), ("Thailand", "China", GB),
    ("Thailand", "Russia", GE), ("Thailand", "London", GC), ("China", "Russia", BE), ("India", "Spain", DH),
    ("India", "London", DC), ("India", "China", DB), ("India", "Russia", DE), ("Brazil", "US", IF),
    ("Brazil", "Spain", IH), ("Spain", "US", HF), ("Spain", "London", FC), ("London", "US", CF)])

dest = input("\nWhere is your final destination\n(Please choose between China, London, Russia, US or Spain only: ")
route = graph.dijkstra("KL", dest)
print("Your shortest route is", route)