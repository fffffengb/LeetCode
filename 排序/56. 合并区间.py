from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: interval[0])
        res = []
        for interval in intervals:
            if len(res) == 0 or (res[-1][1] < interval[0]):
                res.append(interval)
            elif res[-1][1] < interval[1]:
                res[-1][1] = interval[1]

        return res


solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
