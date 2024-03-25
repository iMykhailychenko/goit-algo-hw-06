import networkx as nx
from collections import deque

from data import edges, positions

G = nx.Graph()

for A, B, weight in edges:
    G.add_edge(A, B, weight=weight)


def dfs(start):
    visited = set()
    result = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            stack.extend(G[vertex].keys())
    return result


def bfs(start):
    visited = set()
    result = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(G[vertex]) - visited)
    return result


def distance(path):
    total = 0
    for i in range(1, len(path)):
        current = path[i - 1]
        next = path[i]

        total += G[current].get(next, {}).get("weight", 0)
    return total



if __name__ == "__main__":
    test1 =  dfs("Kyiv")
    print("DFS order:", test1)
    print("DFS distance:", distance(test1), end='\n\n')

    test2 =  bfs("Kyiv")
    print("BFS order:", test2)
    print("BFS distance:", distance(test2))