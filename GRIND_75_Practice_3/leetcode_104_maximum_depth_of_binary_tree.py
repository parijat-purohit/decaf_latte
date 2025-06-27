# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 0
        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return max_depth


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

s = Solution()
print(s.maxDepth(t1))
