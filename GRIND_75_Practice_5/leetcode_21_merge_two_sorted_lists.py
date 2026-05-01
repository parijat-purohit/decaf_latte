"""
Leetcode 21: Merge Two Sorted Lists.
Time Complexity: O(m+n)
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
        if list1 is None and list2 is None:
            return None

        head = temp_head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                temp_head.next = list1
                list1 = list1.next
            else:
                temp_head.next = list2
                list2 = list2.next
            temp_head = temp_head.next

        temp_head.next = list1 or list2
        return head.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)

n1.next = n2
n2.next = n3

n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(5)

n4.next = n5
n5.next = n6

s = Solution()
print(s.mergeTwoLists(n1, n4))
