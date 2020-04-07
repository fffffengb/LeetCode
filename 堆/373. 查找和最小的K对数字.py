from typing import List

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(min_heap, (num1 + num2, [num1, num2]))

        res = []
        while k != 0 and len(min_heap) != 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1

        return res


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 30
solution = Solution()
print(solution.kSmallestPairs(nums1, nums2, k))
