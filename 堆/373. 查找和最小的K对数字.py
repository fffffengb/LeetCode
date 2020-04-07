from typing import List

import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1) == 0 or len(nums2) == 0:
            return None
        min_heap = []
        res = []
        # 先将所有包含nums2[0]的对全部放入堆中, 因为nums1是有序的, 所以它本来就是最小堆
        for num in nums1:
            min_heap.append((num + nums2[0], num, nums2[0], 0))
        while len(min_heap) != 0 and len(res) != k:
            val, num1, num2, index = heapq.heappop(min_heap)
            res.append([num1, num2])
            # 假设当前的(num1, num2)下标为(x, y), 则下一个候选项只会是(x + 1, y)或者(x, y + 1)
            # 由于在最开始已经将所有nums1数据放入堆, 所以只需要判断(x, y + 1)即可
            index += 1
            if index <= len(nums2) - 1:
                num2 = nums2[index]
                candidate = (num1 + num2, num1, num2, index)
                heapq.heappush(min_heap, candidate)
        return res


nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 10
solution = Solution()
print(solution.kSmallestPairs(nums1, nums2, k))
