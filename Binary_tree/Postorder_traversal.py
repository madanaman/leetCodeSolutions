class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        stack = []
        result = []
        if root is None:
            return

        while True:
            while root is not None:
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.right is not None and len(stack) > 0 and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                result.append(root.val)
                root = None

            if len(stack) <= 0:
                break
        return result
