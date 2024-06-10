# 내 풀이

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(visited):
            if sum(visited) > target:
                return

            if sum(visited) == target:
                results.append(visited)
                return
            
            for num in candidates:
                if not visited or visited[-1] <= num:
                    dfs(visited + [num])

        results = []
        dfs([])

        return results