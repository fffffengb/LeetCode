from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        _sum = 0
        for cur_gas, cur_cost in zip(gas, cost):
            cur_tank = cur_gas - cur_cost
            diff.append(cur_tank)
            _sum += cur_tank

        # 如果总油量小于消耗, 则无论从哪个点出发都不够环绕一周
        if _sum < 0:
            return -1

        # 否则一定会有一个点可以环绕一周
        _sum = 0
        start = -1
        for i in range(len(diff)):
            _sum += diff[i]
            # 如果在当前点当前油量小于0, 则此点之前的所有点都不可能是起点
            if _sum < 0:
                _sum = 0
                start = -1
                continue
            # 刚开始计算累加值, 所以将当前点作为起点
            elif start == -1:
                start = i

        return start


all_gas = [2, 3, 4]
all_cost = [3, 4, 3]
solution = Solution()
print(solution.canCompleteCircuit(all_gas, all_cost))
