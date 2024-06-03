# 내 풀이
def maxProfit(self, prices: List[int]) -> int:
    result = 0
    stack = []
    for price in prices:
        if not stack:
            stack.append(price)
        elif stack[-1] > price:
            stack.pop()
            stack.append(price)
        elif stack[-1] < price:
            result = max(result, price - stack[-1])
    return result