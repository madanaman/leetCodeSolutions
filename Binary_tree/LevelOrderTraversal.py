# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        result = []
        result.append([root.val])
        to_be_scanned = [root]
        for level in range(0, 1000):
            temp = []
            for element in to_be_scanned:
                if element.left:
                    temp.append(element.left)
                if element.right:
                    temp.append(element.right)
            if temp.count(None) == len(temp):
                break
            result.append([x.val for x in temp])
            to_be_scanned = temp
        return result