# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.k = k
        self.val = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            self.k -= 1
            if self.k == 0:
                self.val = node.val
            dfs(node.right)
        dfs(root)
        return self.val


t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(1)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t4.left = t6

s = Solution()
print(s.kthSmallest(t1, 3))
