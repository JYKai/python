def solution(nums):
    n = len(nums) // 2
    return n if len(set(nums)) >= n else len(set(nums))
