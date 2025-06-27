from collections import defaultdict, deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        edge_list = {}

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        leaf_nodes = deque([])

        for n in adj_list:
            edge_count = len(adj_list[n])
            edge_list[n] = edge_count
            if edge_count == 1:
                leaf_nodes.append(n)

        while leaf_nodes:
            if n <= 1:
                return list(leaf_nodes)
            queue_length = len(leaf_nodes)
            for _ in range(queue_length):
                node = leaf_nodes.popleft()
                n -= 1
                for neigh in adj_list[node]:
                    edge_list[neigh] -= 1
                    if edge_list[neigh] == 1:
                        leaf_nodes.append(neigh)


s = Solution()
print(s.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
print(s.findMinHeightTrees(3, [[1, 0], [1, 2], [1, 3]]))
print(s.findMinHeightTrees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]))
print(s.findMinHeightTrees(
    8, [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [4, 6], [6, 7]]))
