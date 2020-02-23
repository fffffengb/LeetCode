from typing import List


def calPoints(ops: List[str]) -> int:
    stk = []
    for cur in ops:
        if cur == 'C' and stk.__len__() != 0:
            stk.pop()
        elif cur == 'D':
            stk.append(stk[-1] * 2)
        elif cur == '+':
            stk.append(stk[-1] + stk[-2])
        else:
            stk.append(cur)

    ans = 0
    for val in stk:
        print(type(val), " ", type(ans))
        ans += val

    return ans


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(calPoints(ops))
