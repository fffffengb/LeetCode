from typing import List


class KthLargest:
    _nums: List[int]
    _k: int

    def __init__(self, k: int, nums: List[int]):
        # 先将nums调整成最小堆
        self._nums = nums
        self._k = k
        # 从最后一个有孩子的结点开始
        begin = int((len(nums) - 1) / 2)
        for i in range(begin, -1, -1):
            self.adjust(i, len(nums))
        # 将整个数组中最小的size - k个数放到最后, 这样树根就是第k大的数了
        cnt = 0
        while cnt < len(nums) - k:
            # 交换两个元素
            self._nums[0], self._nums[len(self._nums) - 1 - cnt] = self._nums[len(self._nums) - 1 - cnt], self._nums[0]
            self.adjust(0, len(self._nums) - 1 - cnt)
            cnt += 1

    def add(self, val: int) -> int:
        if len(self._nums) < self._k:
            # 在数组长度小于k的情况下, 将所有元素调整合适
            self.addAndAdjust(val)
        elif self._nums[0] < val:
            self._nums[0] = val
            self.adjust(0, self._k)
        return self._nums[0]

    def adjust(self, i, size):
        while i * 2 + 1 <= size - 1:
            left_index = min_index = i * 2 + 1
            right_index = i * 2 + 2
            # 找出左孩子或左右孩子中较小的那个,
            if right_index <= size - 1 and self._nums[right_index] < self._nums[left_index]:
                min_index = right_index
            # 和当前子树比较, 不符合最小堆则交换
            if self._nums[min_index] < self._nums[i]:
                self._nums[min_index], self._nums[i] = self._nums[i], self._nums[min_index]
            else:
                break
            # 更新下标, 继续循环
            i = min_index

    def addAndAdjust(self, val):
        # 先添加到末尾
        self._nums.append(val)
        # 再调整堆
        child = len(self._nums) - 1
        parent = int((child - 1) / 2)
        # 上滤
        while child != 0 and val < self._nums[parent]:
            self._nums[child] = self._nums[parent]
            child = parent
            parent = int((child - 1) / 2)
        self._nums[child] = val

kthLargest = KthLargest(10, [0])
kthLargest.add(-1)
kthLargest.add(1)
kthLargest.add(-2)
kthLargest.add(4)
kthLargest.add(3)
kthLargest.add(-5)