# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # DFS approach
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """
#         def validate_tree(node, left_val, right_val):
#             if not node:
#                 return True

#             if not (left_val < node.val < right_val):
#                 return False

#             return (validate_tree(node.left, left_val, node.val) and validate_tree(node.right, node.val, right_val))

#         return validate_tree(root, -float('inf'), float('inf'))

# BFS Approach (Using a Queue)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        q = deque([(root, -float('inf'), float('inf'))])

        while q:
            node, left_weight, right_weight = q.popleft()

            if not left_weight < node.val < right_weight:
                return False

            if node.left:
                q.append((node.left, left_weight, node.val))
            if node.right:
                q.append((node.right, node.val, right_weight))
        return True


n1 = TreeNode(8)
n2 = TreeNode(6)
n3 = TreeNode(11)
n4 = TreeNode(7)
n5 = TreeNode(10)

n1.left = n2
n1.right = n3
n2.right = n4
n3.left = n5

s = Solution()
print(s.isValidBST(n1))
