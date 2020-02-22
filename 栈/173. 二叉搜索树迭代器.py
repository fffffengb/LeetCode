class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    stk = []
    root = None

    def __init__(self, root: TreeNode):
        self.root = root

    def next(self) -> int:
        while self.root:
            self.stk.append(self.root)
            self.root = self.root.left
        self.root = self.stk.pop()
        res = self.root.val
        self.root = self.root.right
        return res

    def hasNext(self) -> bool:
        return len(self.stk) != 0
