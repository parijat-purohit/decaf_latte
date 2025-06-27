# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node or node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left if left else right
        return dfs(root)


t1 = TreeNode(3)
t2 = TreeNode(5)
t3 = TreeNode(1)
t4 = TreeNode(6)
t5 = TreeNode(2)
t6 = TreeNode(0)
t7 = TreeNode(8)
t8 = TreeNode(7)
t9 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t5.left = t8
t5.right = t9

s = Solution()
print(s.lowestCommonAncestor(t1, t2, t3))
