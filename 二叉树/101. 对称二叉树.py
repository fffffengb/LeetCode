class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSame(root, root)

    def isSame(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        return root1.val == root2.val \
            and self.isSame(root1.left, root2.right) \
            and self.isSame(root1.right, root2.left)
