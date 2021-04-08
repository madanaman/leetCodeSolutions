# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list_head = None
        new_list_curr_ptr = new_list_head
        l1_curr_ptr = l1
        l2_curr_ptr = l2
        while l1_curr_ptr is not None or l2_curr_ptr is not None:
            print("checking ", l1_curr_ptr.val, l2_curr_ptr.val)
            if l1_curr_ptr.val <= l2_curr_ptr.val:
                value_to_be_added = l1_curr_ptr.val
                if l1_curr_ptr.next is not None:
                    l1_curr_ptr = l1_curr_ptr.next
            else:
                value_to_be_added = l2_curr_ptr.val
                if l2_curr_ptr.next is not None:
                    l2_curr_ptr = l2_curr_ptr.next
            if new_list_curr_ptr is None:
                new_list_head = ListNode(value_to_be_added)
                new_list_curr_ptr = new_list_head
                print("new list initialized")
            else:
                new_list_curr_ptr.next = ListNode(value_to_be_added)
                new_list_curr_ptr = new_list_curr_ptr.next
                print("new list appended with ", new_list_curr_ptr)

        return new_list_head

    def print_list(self, list_head):
        curr_ptr = list_head
        while curr_ptr is not None:
            print(curr_ptr.val)
            curr_ptr = curr_ptr.next

l1elem1 = ListNode(1)
l1elem2 = ListNode(2)
l1elem3 = ListNode(4)
l1elem1.next = l1elem2
l1elem2.next = l1elem3

l2elem1 = ListNode(1)
l2elem2 = ListNode(3)
l2elem3 = ListNode(4)
l2elem1.next = l2elem2
l2elem2.next = l2elem3

solve = Solution()
# solve.print_list(l1elem1)
# solve.print_list(l2elem1)
new_list = solve.mergeTwoLists(l1elem1, l2elem1)