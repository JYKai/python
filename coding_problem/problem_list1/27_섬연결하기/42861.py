def find(parent, n):
    if parent[n] == n: return n
    parent[n] = find(parent, parent[n])
    return parent[n]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    elif rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
    
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    min_cost = 0
    edges = 0
    
    for edge in costs:
        if edges == n - 1:
            break
        
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1
    
    return min_cost
