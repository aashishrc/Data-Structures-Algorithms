# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp!=None:
            count +=1
            temp = temp.next
        if count == 1:
            return None
        elif count == n:
            return head.next
        temp = head
        # i = 1
        k = count - n - 1
        for i  in range(0, k): 
            temp = temp.next
        temp.next = temp.next.next
        return head