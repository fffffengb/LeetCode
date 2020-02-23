from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_arr = []
        # 先构造一个最小值前缀数组
        for num in nums:
            if len(min_arr) == 0 or min_arr[-1] > num:
                min_arr.append(num)
            else:
                min_arr.append(min_arr[-1])
        # 开始从后向前遍历nums
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            while stk and stk[-1] <= min_arr[i]:
                stk.pop()
            if stk and stk[-1] < nums[i]:
                return True
            stk.append(nums[i])
        return False


solution = Solution()
print(solution.find132pattern([6, 12, 3, 4, 6, 11, 20]))
