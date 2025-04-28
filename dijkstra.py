import sys
from collections import defaultdict

def read_graph(filename):
    graph = defaultdict(list)
    with open(filename) as f:
        next(f)  # Skip the first line
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                u, v, w = int(parts[0]), int(parts[1]), float(parts[2])
                graph[u].append((v, w))
                # Add reverse edge if graph is undirected
                graph[v].append((u, w))  # Remove this line if graph is directed
    return graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
        current = min((n for n in distances if n not in visited), key=lambda n: distances[n])
        if distances[current] == float('inf'):
            break
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            if distances[neighbor] > distances[current] + weight:
                distances[neighbor] = distances[current] + weight
    return distances

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: dijkstra.py <file> <start_node>")
        sys.exit(1)
    
    graph = read_graph(sys.argv[1])
    distances = dijkstra(graph, int(sys.argv[2]))
    
    print(f"Shortest distances from node {sys.argv[2]}:")
    for node in sorted(distances):
        print(f"Node {node}: {distances[node] if distances[node] != float('inf') else 'INF'}")
