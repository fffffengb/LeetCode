# class Solution:
#     # "2[ab3[cd]]ef" 我的每一个栈帧中存的是: 3, cd. 他的栈帧中存的是: 3, ab, 所以不用判断栈是否为空.
#     def decodeString(self, s: str) -> str:
#         res = ""
#         stk = []
#         cnt = ""
#         for ch in s:
#             if ch == '[':
#                 stk.append([int(cnt), ""])
#                 cnt = ""
#             elif ch == ']':
#                 cur_res = stk.pop()
#                 if stk:
#                     stk[-1][1] += cur_res[0] * cur_res[1]
#                 else:
#                     res += cur_res[0] * cur_res[1]
#             elif '0' <= ch <= '9':
#                 cnt += ch
#             else:
#                 if stk:
#                     stk[-1][1] += ch
#                 else:
#                     res += ch
#
#         return res

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


solution = Solution()
print(solution.decodeString("ab3[cd]"))
