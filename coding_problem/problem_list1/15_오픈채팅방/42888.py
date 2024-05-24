# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    user = {}
    commands = []
    
    for r in record:
        if r.startswith("Enter"):
            c, u, n = r.split()
            if u not in user:
                user[u] = ""
            user[u] = n
            commands.append((c, u))
        
        elif r.startswith("Leave"):
            c, u = r.split()
            commands.append((c, u))
        
        elif r.startswith("Change"):
            c, u, n = r.split()
            user[u] = n
    
    for command in commands:
        if command[0] == "Enter":
            answer.append(f"{user[command[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{user[command[1]]}님이 나갔습니다.")
            
    return answer