from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def pre(cur: TreeNode, depth: int):
            if cur is None:
                return
            if len(res) < depth:
                res.append([])
            res[depth - 1].append(cur.val)
            pre(cur.left, depth + 1)
            pre(cur.right, depth + 1)

        pre(root, 1)

        return res



