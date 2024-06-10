# 내 풀이
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def DFS(num_list):
            if len(num_list) == len(nums):
                result.append(num_list)
                return
            
            for num in nums:
                if num not in num_list:
                    DFS(num_list + [num])

        result = []
        DFS([])

        return result