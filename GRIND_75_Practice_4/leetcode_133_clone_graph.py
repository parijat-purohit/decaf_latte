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
    
        new_node = Node(node.val)
        q = deque([node])
        node_map = {node: new_node}

        while q:
            curr_node = q.popleft()
            for neigh in curr_node.neighbors:
                if neigh not in node_map:
                    node_map[neigh] = Node(neigh.val)
                    q.append(neigh)
                node_map[curr_node].neighbors.append(node_map[neigh])

        return new_node


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s = Solution()
print(s.cloneGraph(s.cloneGraph(n1)))
