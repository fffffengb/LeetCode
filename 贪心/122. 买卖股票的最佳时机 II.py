from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        while i < len(prices):
            # 先找买入点, 第一次遇到的极小值就是买入点
            while i < len(prices) - 1 and prices[i] > prices[i + 1]:
                i += 1
            low = prices[i]
            # 再找卖出点, 第一次遇到的极大值就是卖出点
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
            height = prices[i]

            res += height - low
            i += 1

        return res


solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))
