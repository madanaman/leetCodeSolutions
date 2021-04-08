class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            new_node = Node(val)
            new_node.prev = curr
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.prev = curr
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
            curr.next.prev = self.head
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.next.prev = curr

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))
# obj = MyLinkedList()
# obj.addAtHead(1)
# print(obj.get(0))
# obj.deleteAtIndex(0)
# print(obj.get(1))
# obj = MyLinkedList()
# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.print_queue()
# obj.addAtIndex(3,0)
# obj.print_queue()
# obj.deleteAtIndex(2)
# obj.print_queue()
# obj.addAtHead(6)
# obj.print_queue()
# obj.addAtTail(4)
# obj.print_queue()
# print(obj.get(4))
# obj.addAtHead(4)
# obj.addAtIndex(5,0)
# obj.addAtHead(6)

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[0],[0]]
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.print_queue()
# obj.addAtIndex(1,2)
# obj.print_queue()
# print("get", obj.get(1))
# obj.deleteAtIndex(0)
# obj.print_queue()
# print("get", obj.get(0))
#
# ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
# [[],[0,10],[0,20],[1,30],[0]]
# obj = MyLinkedList()
# obj.addAtIndex(0,10)
# obj.print_queue()
# obj.addAtIndex(0,20)
# obj.print_queue()
# obj.addAtIndex(0,30)
# print(obj.get(0))
#
# obj = MyLinkedList()
# obj.addAtTail(1)
# obj.print_queue()
# print(obj.get(0))