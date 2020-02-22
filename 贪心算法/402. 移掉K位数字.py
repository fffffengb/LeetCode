class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stk = []
        for ch in num:
            while stk and k != 0 and int(stk[-1]) > int(ch):
                stk.pop()
                k -= 1
            stk.append(ch)
        if k != 0:
            res = "".join(stk[:-k])
        else:
            res = "".join(stk)
        return str(int(res))


solution = Solution()
print(solution.removeKdigits("10200", 5))
