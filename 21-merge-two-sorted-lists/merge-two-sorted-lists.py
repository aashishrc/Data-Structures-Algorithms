# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        cur = ans
        if not list1:
            return list2
        elif not list2:
            return list1
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = ListNode(list1.val)
                list1 = list1.next
            else:
                temp = ListNode(list2.val)  
                list2 = list2.next
            if not ans:
                ans = temp
                cur = ans
            else:
                cur.next = temp
                cur = cur.next
        if list1 == None:
            while list2 != None:
                temp = ListNode(list2.val)  
                cur.next = temp
                cur = cur.next
                list2 = list2.next
        if list2 == None:
            while list1 != None:
                temp = ListNode(list1.val)  
                cur.next = temp
                cur = cur.next
                list1 = list1.next

        return ans