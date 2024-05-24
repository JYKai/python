def solution(money):
    n = len(money)
    
    if n == 1:
        return money[0]
    elif n == 2:
        return max(money)
    
    # 첫 번째 집을 포함하고 마지막 집을 포함하지 않는 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    # 첫 번째 집을 포함하지 않고 마지막 집을 포함하는 경우
    dp2 = [0] * n
    dp2[1] = money[1]
    
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    answer = max(dp1[n-2], dp2[n-1])
    return answer
