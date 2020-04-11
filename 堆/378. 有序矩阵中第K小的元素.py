from typing import List

import heapq


class Solution:
    # 二分法
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            cnt = self.getCnt(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left

    def getCnt(self, matrix, mid) -> int:
        cnt = 0
        n = len(matrix[0])
        for i in range(0, n):
            j = n - 1
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            cnt += j + 1
        return cnt

    # 堆解法
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     max_heap = []
    #     # 维持一个有k个元素的最大堆, 如果新的元素小于堆顶元素, 则pop, push
    #     for one_list in matrix:
    #         for val in one_list:
    #             heapq.heappush(max_heap, -val)
    #             if len(max_heap) > k:
    #                 heapq.heappop(max_heap)
    #     if len(max_heap) != 0:
    #         return -max_heap[0]
    #     else:
    #         return None


mat = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
solution = Solution()
print(solution.kthSmallest(mat, 8))
