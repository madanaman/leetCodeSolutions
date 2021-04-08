# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        temp = []
        curr = head
        if curr is None:
            return False
        elif curr.next is None:
            return True
        #handle zero and 1 element
        while curr is not None:
            temp.append(curr.val)
            curr = curr.next
        if temp[:] == temp[::-1]:
            return True
        else:
            return False