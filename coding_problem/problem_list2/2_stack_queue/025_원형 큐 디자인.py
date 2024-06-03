# 내 풀이
from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.size_q = k
        self.q = deque()

    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.size_q:
            return False
        else:
            self.q.append(value)
            return True

    def deQueue(self) -> bool:
        if not len(self.q):
            return False
        else:
            self.q.popleft()
            return True
        

    def Front(self) -> int:
        if not len(self.q):
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if not len(self.q):
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return True if not len(self.q) else False

    def isFull(self) -> bool:
        return True if len(self.q) == self.size_q else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()