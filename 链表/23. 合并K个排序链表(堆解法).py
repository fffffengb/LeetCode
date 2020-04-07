from typing import List
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildLink(arr):
    cur = head = ListNode(0)
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        cnt = 0
        heap_cnt = 0
        # 将所有头节点放入堆中
        cur = head = ListNode(0)
        for node in lists:
            if node is not None:
                heapq.heappush(min_heap, (node.val, heap_cnt, node))
                heap_cnt += 1

        while len(min_heap) != 0:
            # 从堆顶取出一个节点放入结果集
            val1, val2, cur.next = heapq.heappop(min_heap)
            cur = cur.next
            # 将该节点的下一个节点放入堆中
            if cur.next is not None:
                heapq.heappush(min_heap, (cur.next.val, heap_cnt, cur.next))
                heap_cnt += 1
            else:
                cnt += 1
        return head.next


# lists = [[1,4,5],[1,3,4],[2,6]]
lists = [[], [1]]
links = []
for arr in lists:
    links.append(buildLink(arr))

solution = Solution()
head = solution.mergeKLists(links)
while head.next:
    print(head.val)
    head = head.next
