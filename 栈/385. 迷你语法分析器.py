class NestedInteger:
    pass


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stk = [NestedInteger()]
        num = ""
        for i in range(len(s)):
            if s[i] == '[':
                stk.append(NestedInteger())
            elif s[i] == ',':
                continue
            elif s[i] == ']':
                finishedNestedInteger = stk.pop()
                stk[-1].add(finishedNestedInteger)
            else:
                num += s[i]
                if s[i + 1] == ',' or s[i + 1] == ']':
                    stk[-1].add(NestedInteger(int(num)))
                    num = ""

        return stk.pop().getList()[0]


# 递归
class Solution2:
    s = ""
    i = 0

    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        def getNestedInteger(s: str):
            curNestedInteger = NestedInteger()
            curNum = ""
            while self.i < len(s):
                if s[self.i] == '[':
                    self.i += 1
                    curNestedInteger.add(getNestedInteger(s))
                elif s[self.i] == ',':
                    pass
                elif s[self.i] == ']':
                    return curNestedInteger
                else:
                    curNum += s[self.i]
                    if s[self.i + 1] == ',' or s[self.i + 1] == ']':
                        curNestedInteger.add(NestedInteger(int(curNum)))
                        curNum = ""
                self.i += 1
            return curNestedInteger

        return getNestedInteger(s).getList()[0]
