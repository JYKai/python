# 내 코드
def twoSum(self, nums: List[int], target: int) -> List[int]:
    idx_nums = [[num, idx] for idx, num in enumerate(nums)]
    idx_nums.sort(key=lambda x: x[0])
    
    left, right = 0, len(nums) - 1
    while left < right:
        if idx_nums[left][0] + idx_nums[right][0] == target:
            return [idx_nums[left][1], idx_nums[right][1]]
        elif idx_nums[left][0] + idx_nums[right][0] < target:
            left += 1
        else:
            right -= 1