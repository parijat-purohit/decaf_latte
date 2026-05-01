# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1, t2 = 0, 0

        while (l1):
            t1 = t1*10 + l1.val
            l1 = l1.next

        while (l2):
            t2 = t2*10 + l2.val
            l2 = l2.next

        sum = t1+t2
        list_sum, counter = 0, 0

        while (sum > 0):
            list_sum = list_sum*10 + sum % 10
            sum //= 10
            counter += 1

        dummy = head = ListNode()
        if list_sum == 0:
            return ListNode(0)

        while (counter > 0):
            head.next = ListNode(list_sum % 10)
            head = head.next
            list_sum //= 10
            counter -= 1

        return dummy.next


l1 = ListNode(7)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4

l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(4)

l5.next = l6
l6.next = l7

s = Solution()
print(s.addTwoNumbers(l1, l5))
print(s.addTwoNumbers(ListNode(5), ListNode(5)))
