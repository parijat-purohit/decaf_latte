"""
Leetcode 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Time Complexity: O(M+N)
Space Complexity: O(1)
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = sorted_list = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next
            sorted_list = sorted_list.next
        sorted_list.next = list1 or list2
        return head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)
l1.next = l2
l2.next = l3

l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

s = Solution()
print(s.mergeTwoLists(l1, l4))
