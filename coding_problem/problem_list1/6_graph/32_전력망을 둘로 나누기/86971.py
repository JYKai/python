from collections import defaultdict

def solution(n, wires):
    answer = float('inf')
    
    def DFS(node, visited, graph):
        count = 1
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                count += DFS(next_node, visited, graph)
        return count
    
    tree = defaultdict(list)
    
    for s, e in wires:
        tree[s].append(e)
        tree[e].append(s)
    
    for s, e in wires:
        tree[s].remove(e)
        tree[e].remove(s)
        
        visited = [False] * (n + 1)
        
        count = DFS(s, visited, tree)
        diff = abs(count - (n - count))
        answer = min(diff, answer)
        
        tree[s].append(e)
        tree[e].append(s)
            
    return answer
