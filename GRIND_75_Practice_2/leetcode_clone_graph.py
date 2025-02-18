from collections import deque
# Definition for a Node.


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

        mapped_graph = {}
        mapped_graph[node] = Node(node.val)
        queue = deque([node])

        while queue:
            # This current node is always existing in the new map.
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in mapped_graph:
                    mapped_graph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                mapped_graph[current_node].neighbors.append(
                    mapped_graph[neighbor])

        return mapped_graph[node]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s = Solution()
print(s.cloneGraph(n1))
