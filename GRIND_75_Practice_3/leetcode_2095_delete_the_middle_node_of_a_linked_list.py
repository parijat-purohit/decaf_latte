import math
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head.next is None:
            return None

        if head.next.next is None:
            head.next = None
            return head

        count_head = dummy = head
        counter = 0

        while count_head:
            counter += 1
            count_head = count_head.next

        counter = counter//2 - 1

        while counter >= 1:
            dummy = dummy.next
            counter -= 1

        dummy.next = dummy.next.next

        return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4

s = Solution()
print(s.deleteMiddle(l1))
