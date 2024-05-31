from collections import Counter
import re

data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""

words = re.findall(r'\w+', data)
counter = Counter(words)

print(counter)
"""
Counter({'꽃이': 5, '피네': 3, '산에는': 2, '갈': 2, 
         '봄': 2, '산에': 2, '산에서': 2, '지네': 2, 
         '꽃': 1, '여름없이': 1, '피는': 1, '꽃은': 1, 
         저만치': 1, '혼자서': 1, '피어있네': 1, '우는': 1, 
         '새여': 1, '좋아': 1, '사노라네': 1, '꽃지네': 1, 
         '여름': 1, '없이': 1})
"""

print(counter.most_common(1)) # [('꽃이', 5)]
print(counter.most_common(2)) # [('꽃이', 5), ('피네', 3)]