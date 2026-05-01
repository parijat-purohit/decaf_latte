from collections import deque
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        order = []
        q = deque([root])

        while q:
            temp_order = []
            for _ in range(len(q)):
                node = q.popleft()
                temp_order.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            order.append(temp_order)
        return order


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

s = Solution()
print(s.levelOrder(n1))
