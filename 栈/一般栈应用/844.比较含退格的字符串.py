def get_res(cur_str):
    stk = []
    for ch in cur_str:
        if ch != '#':
            stk.append(ch)
        elif stk.__len__() != 0:
            stk.pop()
    return stk


def backspaceCompare(S: str, T: str) -> bool:
    stk_s = get_res(S)
    stk_t = get_res(T)

    return stk_s == stk_t


print(backspaceCompare("##fd", "##f"))
