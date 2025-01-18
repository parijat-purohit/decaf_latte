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
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        # This following line would propagate a matched node even None
        # towards the root node.
        return left if left else right


n3 = TreeNode(3)
n5 = TreeNode(5)
n1 = TreeNode(1)
n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n7 = TreeNode(7)
n4 = TreeNode(4)

n3.left = n5
n3.right = n1
n5.left = n6
n5.right = n2
n2.left = n7
n2.right = n4
n1.left = n0
n1.right = n8

s = Solution()
print(s.lowestCommonAncestor(n3, n4, n0))
