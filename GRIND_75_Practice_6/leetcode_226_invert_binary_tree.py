"""
leetcode 226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Time Complexity: O(n)
Space Complexity: O(n) It's actually O(h) = O(log n). The tree might be skewed.

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: Optional[TreeNode]
#         """
#         if not root:
#             return

#         st = [root]

#         while st:
#             node = st.pop()
#             if node.left:
#                 st.append(node.left)
#             if node.right:
#                 st.append(node.right)
#             node.left, node.right = node.right, node.left

#         return root

# DFS


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return

        def dfs(node):
            node.left, node.right = node.right, node.left
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return root


s = Solution()
t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(7)
t4 = TreeNode(1)
t5 = TreeNode(3)
t6 = TreeNode(6)
t7 = TreeNode(9)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
print(s.invertTree(t1))
