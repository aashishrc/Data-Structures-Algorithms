# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        temp = head
        count = 0
        while temp != None:
            temp = temp.next
            count +=1
            # print(stack)
        temp = head
        for i in range(count//2):
            temp = temp.next
        last = temp.next
        temp.next = None
        while last != None:
            node = ListNode(last.val)
            stack.append(node)
            last = last.next
        temp = head
        while  temp != None and stack:
            Node = stack.pop()
            t = temp.next
            temp.next = Node
            Node.next = t
            temp = t