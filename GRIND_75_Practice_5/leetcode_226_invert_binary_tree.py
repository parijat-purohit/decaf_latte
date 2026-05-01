# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        def dfs(curr_root):
            if curr_root is None:
                return
            curr_root.left, curr_root.right = curr_root.right, curr_root.left
            dfs(curr_root.left)
            dfs(curr_root.right)

        dfs(root)
        return root


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

s = Solution()
print(s.invertTree(t1))
