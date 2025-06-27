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
        self.k_val = None

        def dfs(node):
            if not node or self.k_val is not None:
                return
            dfs(node.left)

            self.k -= 1
            if self.k == 0:
                self.k_val = node.val

            dfs(node.right)
        dfs(root)
        return self.k_val


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)

t5.left = t3
t5.right = t6
t3.left = t2
t3.right = t4
t2.left = t1

s = Solution()
print(s.kthSmallest(t5, 3))
