def solution(people, limit):
    people.sort()
    count = 0
    i = 0 # 가장 가벼운 사람을 가리키는 인덱스
    j = len(people) - 1 # 가장 무거운 사람을 가리키는 인덱스
    
    while i <= j:
        # 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있으면 태움
        if people[i] + people[j] <= limit:
            i += 1
        # 무거운 사람만 태울 수 있으면 무거운 사람만 보트에 태움
        j -= 1
        count += 1
    return count
