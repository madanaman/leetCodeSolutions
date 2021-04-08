# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def create_ll(self, ip_array):
        head = None
        for i in range(0, len(ip_array)):
            if i == 0:
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

    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = ListNode()
        evens = ListNode()
        odd_head = odds
        even_head = evens

        odd_turn = True

        while head is not None:
            if odd_turn:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            odd_turn = not odd_turn
            head = head.next
        evens.next = None
        odds.next = even_head.next
        return odd_head.next


solve = Solution()
head_of_ll = solve.create_ll([1,2,3,4,5])
print("Start state of list:")
solve.print_ll(head_of_ll)
solve.print_ll(solve.oddEvenList(head_of_ll))