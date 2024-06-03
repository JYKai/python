def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head