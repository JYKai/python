# 내 풀이
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        nums = Counter(nums)
        for items in nums.most_common(k):
            result.append(items[0])
        return result