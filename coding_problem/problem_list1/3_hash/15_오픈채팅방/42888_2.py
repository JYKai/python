def solution(record):
    answer = []
    state = []
    user = {}

    for r in record:
        splited_r = r.split()
        action, user_id = splited_r[0], splited_r[1]

        if action == 'Enter':
            nickname = splited_r[2]
            user[user_id] = nickname  # 최신 닉네임 업데이트
            state.append((action, user_id))
        elif action == 'Leave':
            state.append((action, user_id))
        elif action == 'Change':
            nickname = splited_r[2]
            user[user_id] = nickname  # 닉네임 변경

    for action, user_id in state:
        if action == 'Enter':
            answer.append(f"{user[user_id]}님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(f"{user[user_id]}님이 나갔습니다.")

    return answer
