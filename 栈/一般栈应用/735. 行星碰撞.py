from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for num in asteroids:
            if stk and stk[-1] > 0 and num < 0:
                while stk and 0 < stk[-1] < abs(num):
                    stk.pop()
                # 这时栈可能是空 or 栈顶元素小于0 or 栈顶元素等于abs(num) or 栈顶元素大于abs(num)
                if len(stk) == 0 or stk[-1] < 0:
                    stk.append(num)
                elif stk[-1] == abs(num):
                    stk.pop()
            else:
                stk.append(num)

        return stk


solution = Solution()
print(solution.asteroidCollision([-2, -1, 1, 2]))
