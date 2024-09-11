def solution(graph, source):
    num_nodes = len(graph)

    distances = [float('inf')] * num_nodes
    distances[source] = 0

    pre_nodes = [None] * num_nodes
    pre_nodes[source] = source

    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    pre_nodes[v] = u
    
    for u in range(num_nodes):
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return [-1]
    
    return [distances, pre_nodes]

graph = [[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]]
source = 0

print(solution(graph, source))