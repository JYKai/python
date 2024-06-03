from collections import deque

def build_tree(info, edges):
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
    return tree

def solution(info, edges):
    answer = 0
    trees = build_tree(info, edges)
    
    q = deque()
    q.append([0, 1, 0, set()])
    
    while q:
        current, sheep, wolf, visited = q.popleft()
        answer = max(answer, sheep)
        visited.update(trees[current])
        for next_visit in visited:
            if info[next_visit] != 0:
                if sheep != wolf + 1:
                    q.append([next_visit, sheep, wolf + 1, visited - {next_visit}])
            else:
                q.append([next_visit, sheep + 1, wolf, visited - {next_visit}])
                
    return answer
