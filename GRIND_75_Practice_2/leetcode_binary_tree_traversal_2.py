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
        q = deque([(root, 0)])
        result = []

        while q:
            node, depth = q.popleft()
            if depth == len(result):
                result.append([])
            result[depth].append(node.val)

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return result


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n7

s = Solution()
print(s.levelOrder(n1))
