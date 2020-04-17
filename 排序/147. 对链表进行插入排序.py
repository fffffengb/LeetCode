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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        pre = head
        while pre.next is not None:
            cur = pre.next
            if cur.val < pre.val:
                # 删除cur这个节点
                pre.next = cur.next
                # 如果cur是最小的节点
                if head.val > cur.val:
                    cur.next = head
                    head = cur
                else:
                    # 从头开始遍历链表, 找一个合适的位置
                    temp = head
                    while temp.next is not None and temp.next.val <= cur.val:
                        temp = temp.next
                    # 插入cur
                    cur.next = temp.next
                    temp.next = cur
            else:
                pre = pre.next

        return head


arr = [-1, 5, 3, 4, 0]
head = buildLink(arr)
solution = Solution()
head = solution.insertionSortList(head)
while head:
    print(head.val)
    head = head.next
