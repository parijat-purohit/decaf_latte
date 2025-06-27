# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        self.balanced = True

        def height(node):
            if not node:
                return 0
            left = 1 + height(node.left)
            right = 1 + height(node.right)
            if abs(left - right) > 1:
                self.balanced = False
            return max(left, right)
        height(root)
        return self.balanced


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.right = t5
t5.right = t4

s = Solution()
print(s.isBalanced(t1))
