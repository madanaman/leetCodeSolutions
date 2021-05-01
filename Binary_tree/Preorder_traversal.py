# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def build_dq(self, left_ptr, right_ptr, queue: deque):
        if right_ptr:
            queue.appendleft(right_ptr)
        if left_ptr:
            queue.appendleft(left_ptr)

    def preorderTraversal(self, root: TreeNode):
        processed = []
        dq = deque()
        if root is None:
            return processed
        if root.left is None and root.right is None:
            return [root.val]
        processed.append(root.val)
        left_ptr = root.left
        right_ptr = root.right
        self.build_dq(left_ptr=left_ptr, right_ptr=right_ptr, queue=dq)
        while len(dq) > 0:
            item = dq.popleft()
            processed.append(item.val)
            left_ptr = item.left
            right_ptr = item.right
            self.build_dq(left_ptr=left_ptr, right_ptr=right_ptr, queue=dq)

        return processed