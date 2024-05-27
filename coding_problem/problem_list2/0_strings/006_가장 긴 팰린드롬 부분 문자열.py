# 내 코드

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest = 0
        result = []
        for step in range(1, len(s) + 1):
            for i in range(len(s) - step + 1):
                if s[i: i + step] == s[i: i + step][::-1]:
                    longest = step
                    result.append(s[i: i + step])
                    break
        
        return result[-1]