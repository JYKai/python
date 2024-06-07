# 내 풀이

from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        stones = Counter(stones)
        for jewel in jewels:
            result += stones[jewel]
        return result