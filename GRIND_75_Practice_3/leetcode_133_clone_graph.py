# Definition for a Node.
from collections import deque


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        old_to_new_graph = {}
        old_to_new_graph[node] = Node(node.val)

        queue = deque([node])

        while queue:
            old_node = queue.popleft()

            for neighbor in old_node.neighbors:
                if neighbor not in old_to_new_graph:
                    old_to_new_graph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new_graph[old_node].neighbors.append(
                    old_to_new_graph[neighbor])
        return old_to_new_graph[node]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = ([n2, n4])
n2.neighbors = ([n1, n3])
n3.neighbors = ([n2, n4])
n4.neighbors = ([n1, n3])

s = Solution()
print(s.cloneGraph(n1))
