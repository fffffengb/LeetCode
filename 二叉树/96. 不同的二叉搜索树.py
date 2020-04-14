class Solution:
    def numTrees(self, n: int) -> int:
        res = [0 for _ in range(n + 1)]
        res[0] = res[1] = 1
        for i in range(2, n + 1):
            for root in range(1, i + 1):
                res[i] += res[root - 1] * res[i - root]

        return res[-1]


solution = Solution()
print(solution.numTrees(50))
