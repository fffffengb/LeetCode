from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        step = 1
        num = len(lists)
        while step < num:
            for i in range(0, num - 1, step * 2):
                if i + step <= num - 1:
                    lists[i] = self.merge2Lists(lists[i], lists[i + step])
            step *= 2
        return lists[0]

    def merge2Lists(self, list1: ListNode, list2: ListNode):
        cur = head = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 is not None:
            cur.next = list1
        if list2 is not None:
            cur.next = list2
        return head.next


def buildLink(arr):
    cur = head = ListNode(0)
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return head.next


lists = [[-9, -7, -7], [-6, -4, -1, 1], [-6, -5, -2, 0, 0, 1, 2], [-9, -8, -6, -5, -4, 1, 2, 4], [-10], [-5, 2, 3]]
# lists = []
links = []
for arr in lists:
    links.append(buildLink(arr))

solution = Solution()
head = solution.mergeKLists(links)
while head:
    print(head.val)
    head = head.next
