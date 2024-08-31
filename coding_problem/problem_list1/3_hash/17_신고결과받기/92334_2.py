from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reporter_dict = defaultdict(set)
    reported_dict = defaultdict(int)
    
    for r in report:
        reporter, reported = r.split()
        if reported not in reporter_dict[reporter]:
            reported_dict[reported] += 1
        reporter_dict[reporter].add(reported)
    
    for idx, _id in enumerate(id_list):
        for reported in reporter_dict[_id]:
            if reported_dict[reported] >= k:
                answer[idx] += 1
    
    return answer
