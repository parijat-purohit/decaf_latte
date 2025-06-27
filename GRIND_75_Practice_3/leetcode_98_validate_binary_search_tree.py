# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(lb, root, ub):
            if not root:
                return True
            if not (lb < root.val < ub):
                return False
            return (validate(lb, root.left, root.val) and validate(root.val, root.right, ub))

        return validate(-float('inf'), root, float('inf'))


t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)

t1.left = t3
t1.right = t2

s = Solution()
print(s.isValidBST(t1))
