class NestedInteger:
    pass


# 注意这两个测试用例: [], [[],[3]]
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stk = [nestedList]
#
#     def next(self) -> int:
#         return self.stk.pop().getInteger()
#
#     def hasNext(self) -> bool:
#         while len(self.stk) != 0 and isinstance(self.stk[-1], list):
#             top = self.stk.pop()
#             for i in range(len(top) - 1, -1, -1):
#                 if not top[i].isInteger():
#                     top[i] = top[i].getList()
#                 self.stk.append(top[i])
#         return len(self.stk) != 0

# 更契合题意的解法
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stk = [nestedList]

    def next(self) -> int:
        return self.stk.pop().getInteger()

    def hasNext(self) -> bool:
        while len(self.stk) != 0 and isinstance(self.stk[-1], list):
            top = self.stk.pop()
            for i in range(len(top) - 1, -1, -1):
                if not top[i].isInteger():
                    top[i] = top[i].getList()
                self.stk.append(top[i])
        return len(self.stk) != 0