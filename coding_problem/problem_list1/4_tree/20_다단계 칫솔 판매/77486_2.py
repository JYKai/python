from collections import defaultdict

def solution(enroll, referral, seller, amount):
    orga = defaultdict(str)
    earning = dict()
    
    for enr, ref in zip(enroll, referral):
        orga[enr] = ref
        earning[enr] = 0
    earning['-'] = 0
    
    for sel, amo in zip(seller, amount):
        money = amo * 100
        change = money // 10
        earning[sel] += (money - change)
        while orga[sel] != '-' and change > 0:
            sel = orga[sel]
            money = change
            change = money // 10
            earning[sel] += (money - change)
    
    return [earning[name] for name in enroll]
