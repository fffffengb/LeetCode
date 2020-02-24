from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        temp = [-1 for i in range(size * 2)]
        nums.extend(nums)
        stk = []
        for i in range(size * 2):
            while stk and nums[stk[-1]] < nums[i]:
                temp[stk.pop()] = nums[i]
            stk.append(i)
        return temp[:size]

solution = Solution()
print(solution.nextGreaterElements([1,2,1]))