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
        self.balanced = True

        def dfs(node):
            if node is None:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.balanced


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t2.left = t3
t3.left = t4
t1.right = t5

s = Solution()
print(s.isBalanced(t1))
