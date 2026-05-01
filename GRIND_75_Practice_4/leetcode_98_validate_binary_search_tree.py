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
        self.valid = True

        def validate(left, node, right):
            if not node:
                return
            if node.val <= left or node.val >= right:
                self.valid = False
                return
            validate(left, node.left, node.val)
            validate(node.val, node.right, right)

        validate(-float('inf'), root, float('inf'))
        return self.valid


n1 = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(3)
n5 = TreeNode(6)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

# n1 = TreeNode(2)
# n2 = TreeNode(1)
# n3 = TreeNode(3)

# n1.left = n2
# n1.right = n3

s = Solution()
print(s.isValidBST(n1))
