def removeOuterParentheses(S: str) -> str:
    stk = []
    left = '('
    res = ""
    start = 0

    for i in range(len(S)):
        if S[i] == left:
            stk.append(left)
        else:
            stk.pop()

        if len(stk) == 0:
            res += S[start + 1: i]
            start = i + 1

    return res


print(removeOuterParentheses("(()())(())(()(()))"))
