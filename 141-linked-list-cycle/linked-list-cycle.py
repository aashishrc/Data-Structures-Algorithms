# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        prev = head
        cur = head.next
        while prev and cur and prev != cur:
            if prev.next:
                prev = prev.next
            else:
                return False
            if cur.next:
                cur = cur.next.next
            else:
                return False
        if prev == cur:
            return True