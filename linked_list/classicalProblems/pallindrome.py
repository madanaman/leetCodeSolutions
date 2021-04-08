# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addToHead(self, list_head, val):
        new_node = ListNode(val)
        if list_head is None:
            list_head = new_node
        else:
            new_node.next = list_head
            list_head = new_node
        return list_head

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False
        if head.next is None:
            return True
        newList_head = None
        curr = head
        while curr is not None:
            newList_head = self.addToHead(newList_head, curr.val)
            curr = curr.next

        org_list_ptr = head
        new_list_ptr = newList_head
        Fail = False
        while org_list_ptr is not None and not Fail:
            if org_list_ptr.val != new_list_ptr.val:
                Fail = True
                break
            else:
                org_list_ptr = org_list_ptr.next
                new_list_ptr = new_list_ptr.next

        return not Fail
