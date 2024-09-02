def solution(enroll, referral, seller, amount):
    organization = {}
    calculate = {}
    first = enroll[0]
    
    for e, r in zip(enroll, referral):
        organization[e] = r
        calculate[e] = 0
    
    def DFS(calcu, n, money):
        if n == '-':
            return
        
        else:
            if money // 10 == 0:
                calcu[n] += money
            else:
                calcu[n] += (money - money // 10)
                DFS(calcu, organization[n], money // 10)
            
    for s, a in zip(seller, amount):
        DFS(calculate, s, a * 100)
    
    return list(calculate.values())
