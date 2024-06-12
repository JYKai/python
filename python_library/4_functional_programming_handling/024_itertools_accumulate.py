import itertools

monthly_income = [1123, 1242, 5322, 1242, 3212, 5224, 6642, 3232, 2211, 2153]
result = list(itertools.accumulate(monthly_income))

print(result) # [1123, 2365, 7687, 8929, 12141, 17365, 24007, 27239, 29450, 31603]

result = list(itertools.accumulate(monthly_income, max))

print(result) # [1123, 1242, 5322, 5322, 5322, 5322, 6642, 6642, 6642, 6642]