from collections import deque


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

        queue = deque([root])
        result = []
        while queue:
            level = []
            queue_length = len(queue)

            for _ in range(queue_length):
                print(queue)
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                result.append(level)

        return result


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

s = Solution()
print(s.levelOrder(t1))
