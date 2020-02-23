class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stk = []
        for ch in preorder:
            if ch != '#':
                stk.append(ch)
            else:
                while stk and stk[-1] == '#':
                    stk.pop()
                    if stk:
                        stk.pop()
                    else:
                        return False
                stk.append(ch)
        return stk == ['#']


# solution = Solution()
# print(solution.isValidSerialization("#"))
stk = [[]]
print(isinstance(stk[-1], list))
