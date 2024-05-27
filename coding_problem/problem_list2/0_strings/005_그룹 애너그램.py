# 내 코드
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        ana_dict = defaultdict(list)
        for word in strs:
            temp = sorted(word)
            ana_dict[''.join(temp)].append(word)
        
        for value in ana_dict.values():
            answer.append(sorted(value))

        answer.sort(key=lambda x: len(x))
        return answer