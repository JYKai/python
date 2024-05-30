# 내 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    vals = []

    if not head:
        return True

    node = head
    while node is not None:
        vals.append(node.val)
        node = node.next

    return vals == vals[::-1]