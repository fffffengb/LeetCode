import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        mark = {1: 1}
        res = []
        for i in range(1690):
            cur_val = heapq.heappop(min_heap)
            res.append(cur_val)
            # 把堆顶元素和origin中的每一个元素相乘并放入堆中
            for val in [2, 3, 5]:
                new_val = val * cur_val
                if mark.get(new_val) is None:
                    mark[new_val] = 1
                    heapq.heappush(min_heap, new_val)
        return res[n - 1]


solution = Solution()
print(solution.nthUglyNumber(1690))

