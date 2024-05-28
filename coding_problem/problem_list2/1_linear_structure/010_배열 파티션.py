# 내 풀이
def arrayPairSum(self, nums: List[int]) -> int:
    result = 0

    nums = sorted(nums, reverse=True)
    for i in range(0, len(nums), 2):
        result += min(nums[i: i + 2])

    return result