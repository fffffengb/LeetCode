from typing import List


class Solution:
    stones: List[int]

    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        self.stones = stones
        # 最后一个有孩子的节点下标
        last_root = (len(self.stones) - 2) // 2
        # 调整成最大堆
        for i in range(last_root, -1, -1):
            self.down_filter(i, len(self.stones))
        # 循环删除两个节点, 再添加一个节点(如果有的话)
        temp = []
        # while len(self.stones) > 0:
        #     if len(temp) < 2:
        #         temp.append(self.stones[0])
        #         self.stones[0] = self.stones[-1]
        #         self.stones.pop()
        #         self.down_filter(0, len(self.stones))
        #     if len(temp) == 2:
        #         val = abs(temp[0] - temp[1])
        #         temp.clear()
        #         if val != 0:
        #             self.addAndAdjust(val)
        # if len(temp) == 1:
        #     return temp[0]
        # else:
        #     return 0

        while len(self.stones) > 0:
            if len(self.stones) == 1:
                return self.stones[0]
            val1 = self.popAndAdjust()
            val2 = self.popAndAdjust()
            if val1 != val2:
                self.addAndAdjust(abs(val1 - val2))

        return 0

    def popAndAdjust(self) -> int:
        val = self.stones[0]
        self.stones[0] = self.stones[-1]
        self.stones.pop()
        self.down_filter(0, len(self.stones))
        return val

    def down_filter(self, root: int, size: int):
        while root * 2 + 1 <= size - 1:
            max_child = left_child = root * 2 + 1
            right_child = left_child + 1
            if right_child <= size - 1 and self.stones[right_child] > self.stones[left_child]:
                max_child = right_child
            if self.stones[root] >= self.stones[max_child]:
                break
            else:
                self.stones[root], self.stones[max_child] = self.stones[max_child], self.stones[root]
            root = max_child

    def addAndAdjust(self, val: int):
        self.stones.append(val)
        child = len(self.stones) - 1
        while child > 0:
            parent = (child - 1) // 2
            if self.stones[parent] < val:
                self.stones[child] = self.stones[parent]
            else:
                break
            child = parent
        self.stones[child] = val


solution = Solution()
print(solution.lastStoneWeight([0, 1]))
