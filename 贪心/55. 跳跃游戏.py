from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        end = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # 如果当前元素可以到达end, 则更新end
            if nums[i] >= end - i:
                end = i

        if end == 0:
            return True
        else:
            return False
