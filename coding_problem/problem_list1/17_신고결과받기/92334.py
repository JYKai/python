# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_id = {}
    reported_id = {}
    for id in id_list:
        report_id[id] = set()
        reported_id[id] = set()
    
    for r in report:
        f, s = r.split()
        report_id[f].add(s)
        reported_id[s].add(f)
    
    banned = []
    for key, values in reported_id.items():
        if len(values) >= k:
            banned.append(key)
    
    for idx, member in enumerate(id_list):
        check_list = report_id[member]
        for check in check_list:
            if check in banned:
                answer[idx] += 1
                
    return answer