# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def create_ll(self,ip_array):
        head = None
        for i in range(0, len(ip_array)):
            if i == 0:
                print('first element added')
                head = ListNode(ip_array[i])
            else:
                curr = head
                while curr.next is not None:
                    curr = curr.next
                curr.next = ListNode(ip_array[i])

        return head

    def print_ll(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next

    def removeElements(self, head, val):
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


solve = Solution()
head = solve.create_ll([1,2,6,3,4,5,6])
# solve.print_ll(head)
solve.print_ll(solve.removeElements(head, 6))