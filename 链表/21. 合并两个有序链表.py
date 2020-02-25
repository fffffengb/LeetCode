class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     head = ListNode(0)
    #     cur = head
    #     while l1 and l2:
    #         if l1.val < l2:
    #             new_node = ListNode(l1.val)
    #             l1 = l1.next
    #         else:
    #             new_node = ListNode(l2.val)
    #             l2 = l2.next
    #         cur.next = new_node
    #         cur = cur.next
    #     if l1:
    #         cur.next = l1
    #     if l2:
    #         cur.next = l2
    #     return head.next
    # [2]
    # [1,3,4, 5, 6]
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def getLink(arr):
    head = ListNode(0)
    cur = head
    for num in arr:
        new_node = ListNode(num)
        cur.next = new_node
        cur = cur.next
    return head.next


list1 = getLink([2, 4])
list2 = getLink([1, 3, 4, 5, 6])

solution = Solution()
head = solution.mergeTwoLists(list1, list2)
while head:
    print(head.val)
    head = head.next
