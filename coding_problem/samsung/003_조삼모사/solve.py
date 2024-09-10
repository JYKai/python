from itertools import combinations

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
works = list(range(n))

combi_list = list(combinations(works, len(works) // 2))

mini = float('inf')
for combi in combi_list:
    morning_score = 0
    evening_score = 0

    morning_team = combi
    evening_temp = [x for x in works if x not in morning_team]
   
    for i in range(len(morning_team)):
        for j in range(i + 1, len(morning_team)):
            morning_score += (maps[morning_team[i]][morning_team[j]] + maps[morning_team[j]][morning_team[i]])
    
    for i in range(len(evening_temp)):
        for j in range(i + 1, len(evening_temp)):
            evening_score += (maps[evening_temp[i]][evening_temp[j]] + maps[evening_temp[j]][evening_temp[i]])

    mini = min(mini, abs(morning_score - evening_score))

print(mini)