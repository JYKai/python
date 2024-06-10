# 내 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(subset):
            
            result.append(subset)

            for num in nums:
                if not subset or subset[-1] < num:
                    dfs(subset + [num])

        dfs([])
        return result