class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        start_head = head
        curr_ptr = head.next
        while start_head.next is not None:
            temp = curr_ptr.next
            start_head.next = curr_ptr.next
            curr_ptr.next = head
            head = curr_ptr
            curr_ptr = temp
        return head
