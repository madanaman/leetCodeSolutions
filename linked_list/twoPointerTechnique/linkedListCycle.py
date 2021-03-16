# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        ptr1 = head
        pos = 0
        ptr2 = head.next
        while ptr1 is not None and ptr2 is not None:
            if ptr1 == ptr2:
                return True
            elif ptr1.next is not None and ptr2.next is not None:
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next
                if ptr1 == ptr2:
                    return True
                if ptr1 == head:
                    pos = 0
                else:
                    pos += 1
            else:
                return False