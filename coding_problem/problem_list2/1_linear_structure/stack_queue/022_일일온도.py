# 내 코드
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    results = [0] * len(temperatures)
    for idx, temp in enumerate(temperatures):
        if not stack or stack[-1][1] > temp:
            stack.append((idx, temp))
        else:
            while stack and stack[-1][1] < temp:
                before_idx, before_temp = stack.pop()
                results[before_idx] = idx - before_idx
            stack.append((idx, temp))

    return results