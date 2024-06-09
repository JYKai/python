# 내 풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(L, word_list):
            if L == len(digits):
                results.append(''.join(word_list))
                return
            
            else:
                for char in numbers[digits[L]]:
                    dfs(L + 1, word_list + [char])

        numbers = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        
        results = []
        dfs(0, [])
        return results