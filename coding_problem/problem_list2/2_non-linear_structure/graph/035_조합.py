# 내 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def DFS(start, visited):
            if len(visited) == k:
                result.append(visited)
                return 
            
            for num in range(start + 1, n + 1):
                if visited[-1] < num:
                    DFS(start + 1, visited + [num])
        
        result = []
        for num in range(1, n + 1):
            DFS(num, [num])

        return result