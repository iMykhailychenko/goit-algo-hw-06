import networkx as nx
from tabulate import tabulate

from data import edges, cities

G = nx.Graph()

for A, B, weight in edges:
    G.add_edge(A, B, weight=weight)


def dijkstra(start):
    distances = {vertex: float('infinity') for vertex in G}
    distances[start] = 0
    unvisited = list(G)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, attr in G[current_vertex].items():
            distance = distances[current_vertex] + attr["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(current_vertex)
    return distances


if __name__ == "__main__":
    data = []
    
    for city in cities:
        result = sorted(list(dijkstra(city).items()), key=lambda x: x[1])
        row = [f"{x[0]} ({x[1]})" for x in result]
        row.append(sum(x for _, x in result))
        data.append(row)

    print(tabulate(data, tablefmt="pipe"))