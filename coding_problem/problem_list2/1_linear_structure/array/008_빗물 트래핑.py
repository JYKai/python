def trap(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()
            if not len(stack):
                break
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        
        total = 0
        while left < right:
            if left_max <= right_max:
                total += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                total += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
                
        return total