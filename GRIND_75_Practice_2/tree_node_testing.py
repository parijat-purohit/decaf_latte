class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countLeafNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.counter = 0

        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                self.counter += 1
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.counter


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)

t1.left = t2
t2.left = t3
t3.left = t4
t4.left = t5
t5.left = t6

s = Solution()
print(s.countLeafNodes(t1))
