from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stk = []
        while root is not None or stk:
            while root is not None:
                stk.append(root)
                root = root.left

            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stk = [[0, root]]
        while stk:
            flag, cur = stk.pop()
            if cur is None:
                continue
            if flag == 0:
                stk.append([0, cur.right])
                stk.append([1, cur])
                stk.append([0, cur.left])
            else:
                res.append(cur.val)

        return res


i = 0
tree = [1, 2, '#', '#', 3, 4, '#', '#', 5, '#', '#']
def buildTree():
    global i
    global tree
    val = tree[i]
    i += 1
    if val == '#':
        return
    root = TreeNode(val)
    root.left = buildTree()
    root.right = buildTree()
    return root


root = buildTree()
solution = Solution()
print(solution.inorderTraversal2(root))
