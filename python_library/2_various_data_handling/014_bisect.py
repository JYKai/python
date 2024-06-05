# import bisect

# result = []

# for score in [33, 99, 77, 70, 89, 90, 100]:
#     pos = bisect.bisect([60, 70, 80, 90], score) # 0, 4, 2, 2, 3, 4, 4
#     grade = 'FDCBA'[pos]
#     result.append(grade)

# print(result) # ['F', 'A', 'C', 'C', 'B', 'A', 'A']

####################################################################################

import bisect

result = []

for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score) # 0, 4, 2, 1, 3, 3, 4
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result) # ['F', 'A', 'C', 'D', 'B', 'B', 'A']