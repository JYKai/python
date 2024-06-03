# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    total = len(prices)
    answer = [0] * total
    stack = []
    for idx, price in enumerate(prices, start=1):
        if not stack:
            stack.append([price, idx])
        else:
            if stack[-1][0] <= price:
                stack.append([price, idx])
            else:
                while stack and stack[-1][0] > price:
                    before_price, before_idx = stack.pop()
                    answer[before_idx - 1] = idx - before_idx
                stack.append([price, idx])

    while stack:
        before_price, before_idx = stack.pop()
        answer[before_idx - 1] = total - before_idx
    return answer