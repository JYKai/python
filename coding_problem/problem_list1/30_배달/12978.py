from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    
    road_dict = defaultdict(list)
    for s, e, c in road:
        road_dict[s].append([e, c])
        road_dict[e].append([s, c])
        
    towns = [float('inf')] * (N + 1)
    towns[1] = 0
    
    q = []
    heapq.heappush(q, [towns[1], 1])
    
    while q:
        current_distance, current_town = heapq.heappop(q)

        if current_distance > towns[current_town]:
            continue
            
        for adjacent_town, cost in road_dict[current_town]:
            distance = cost + current_distance
            if distance < towns[adjacent_town]:
                towns[adjacent_town] = distance
                heapq.heappush(q, [distance, adjacent_town])

    for town in towns[1:]:
        if town <= K:
            answer += 1
            
    return answer
