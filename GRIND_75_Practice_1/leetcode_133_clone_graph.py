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

        new_graph_store = {}
        new_graph_store[node] = Node(node.val)
        # we would always store the nodes from the origin graph into
        # the queue and they are already copied into the new store.
        queue = deque([node])

        while queue:
            c_node = queue.popleft()

            for neighbor in c_node.neighbors:
                if neighbor not in new_graph_store:
                    new_graph_store[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                new_graph_store[c_node].neighbors.append(
                    new_graph_store[neighbor])

        return new_graph_store[node]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s = Solution()
s.cloneGraph(n1)
