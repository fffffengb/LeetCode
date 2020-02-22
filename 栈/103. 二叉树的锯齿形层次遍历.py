from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 直接BFS
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        cur_level = [root]
        deep = 0
        res = []
        while cur_level:
            temp = []
            next_level = []
            for node in cur_level:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if deep % 2 == 0:
                res.append(temp)
            else:
                temp.reverse()
                res.append(temp)
            cur_level = next_level
            deep += 1
        return res

    tree_map = None
    # 先递归层序遍历,再逆序输出
    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        self.tree_map = [[] for i in range(30)]
        self.getTreeMap(root, 0)
        res = []
        for i in range(len(self.tree_map)):
            if not self.tree_map[i]:
                break
            if i % 2 == 0:
                res.append(self.tree_map[i])
            else:
                self.tree_map[i].reverse()
                res.append(self.tree_map[i])
        return res

    def getTreeMap(self, root, deep):
        if root is None:
            return
        self.tree_map[deep].append(root.val)
        self.getTreeMap(root.left, deep + 1)
        self.getTreeMap(root.right, deep + 1)


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
print(solution.zigzagLevelOrder(root))
