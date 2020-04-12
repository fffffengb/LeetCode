from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.getTree(1, n)

    def getTree(self, low, height) -> List[TreeNode]:
        if low > height:
            return [None]
        if low == height:
            return [TreeNode(height)]
        res = []
        for i in range(low, height + 1):
            left_tree = self.getTree(low, i - 1)
            right_tree = self.getTree(i + 1, height)
            for left in left_tree:
                for right in right_tree:
                    cur_root = TreeNode(i)
                    cur_root.left = left
                    cur_root.right = right
                    res.append(cur_root)

        return res


solution = Solution()
solution.generateTrees(0)
