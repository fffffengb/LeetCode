from typing import List

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        # 维持一个有k个元素的最大堆, 如果新的元素小于堆顶元素, 则pop, push
        for one_list in matrix:
            for val in one_list:
                heapq.heappush(max_heap, -val)
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        if len(max_heap) != 0:
            return -max_heap[0]
        else:
            return None
