def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    for splited_s in s:
        for split in splited_s.split(','):
            if int(split) not in answer:
                answer.append(int(split))
    return answer
