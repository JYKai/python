def solution(strs, t):
    n = len(t)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    str_set = set(strs)
    
    for i in range(1, n + 1):
        for size in range(1, 6):
            if (i - size >= 0 and t[i - size: i] in str_set):
                dp[i] = min(dp[i], dp[i - size] + 1)

    return dp[-1] if dp[-1] < float('inf') else -1