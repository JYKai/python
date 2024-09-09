from collections import defaultdict

def solution(info, edges):
    answer = 0
    
    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    def DFS(node, visited, sheep, wolf):
        nonlocal answer
        if sheep > answer:
            answer = sheep
            
        visited.update(tree[node])
        
        for next_node in visited:       
            if info[next_node] == 1:
                if wolf + 1 < sheep:
                    DFS(next_node, visited - {next_node}, sheep, wolf + 1)
            else:
                DFS(next_node, visited - {next_node}, sheep + 1, wolf)
    
    DFS(0, set(), 1, 0)
        
    return answer
