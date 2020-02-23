class Solution:
    def parseTernary(self, expression: str) -> str:
        # 用来标记下一个遇到的字符是条件
        is_condition = 0
        stk = []
        # 因为是从右至左结合,所以也从右至左遍历
        for i in range(len(expression) - 1, -1, -1):
            if expression[i] == ':':
                continue
            elif expression[i] == '?':  # 标记下一个遇到的字符是条件
                is_condition = 1
            else:
                if is_condition:
                    if expression[i] == 'T':  # 说明栈中的第一个元素是结果, 但要把错误结果删掉
                        res = stk[-1]
                        stk.pop()
                        stk.pop()
                        stk.append(res)
                    else:  # 说明栈中第二个元素是结果, 删掉栈顶元素即可
                        stk.pop()
                    is_condition = 0
                else:  # 当前扫描到的元素不是条件, 就是直接入栈
                    stk.append(expression[i])
        return stk[-1]


solution = Solution()
print(solution.parseTernary("F ? 1 : T?4:5"))
