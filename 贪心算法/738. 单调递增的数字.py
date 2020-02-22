class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        num_str = str(N)
        stk = []
        i = 1
        while i < len(num_str):
            stk.append(num_str[i - 1])

            if int(num_str[i - 1]) > int(num_str[i]):
                cur = int(num_str[i - 1]) - 1
                while stk and int(stk[-1]) > cur:
                    cur = int(stk.pop()) - 1
                stk.append(str(cur))
                break

            if i == len(num_str) - 1:
                stk.append(num_str[i])

            i += 1
        res = ""
        for ch in stk:
            res += ch
        res += (len(num_str) - len(stk)) * '9'
        return int(res)


solution = Solution()
print(solution.monotoneIncreasingDigits(332))
