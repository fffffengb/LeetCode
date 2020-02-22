from typing import List


def isOperator(ch: str) -> bool:
    if ch in ['+', '-', '*', '/']:
        return True
    return False


def calculate(val1, val2, operator):
    if operator == '+':
        return val1 + val2
    if operator == '-':
        return val2 - val1
    if operator == '*':
        return val1 * val2
    if operator == '/':
        return int(val2 / val1)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for ch in tokens:
            if isOperator(ch):
                val1 = int(stk.pop())
                val2 = int(stk.pop())
                res = calculate(val1, val2, ch)
                stk.append(res)
            else:
                stk.append(int(ch))
        return stk.pop()


# solution = Solution()
# print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
# print(solution.evalRPN(["4", "13", "5", "/", "+"]))

queue = [1, 2, 3]
print(queue.pop(0))