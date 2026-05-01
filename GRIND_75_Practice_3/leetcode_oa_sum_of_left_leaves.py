from collections import deque
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.sum = 0
        left_node = []
        queue = deque([root])
        while (queue):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                left_node.append(node.left)
            if node.right:
                queue.append(node.right)
            elif not node.left and node in left_node:
                self.sum += node.val
        return self.sum


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

# t1 = TreeNode(1)

s = Solution()
print(s.sumOfLeftLeaves(t1))
