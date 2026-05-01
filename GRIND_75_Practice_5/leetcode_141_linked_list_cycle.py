"""
Leetcode 141: Linked List Cycle
Time Complexity: O(length of the linked list)
Space Complexity: O(1)
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        fast_ptr = head.next.next
        slow_ptr = head.next

        while fast_ptr and fast_ptr.next:
            if fast_ptr == slow_ptr:
                return True
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next


l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

s = Solution()
print(s.hasCycle(l1))
