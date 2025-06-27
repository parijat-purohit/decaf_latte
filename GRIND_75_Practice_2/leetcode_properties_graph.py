from collections import defaultdict


class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)

        def intersects(a, b):
            return len(set(a) & set(b))

        for i in range(len(properties)):
            edge = False
            for j in range(i+1, len(properties)):
                if intersects(properties[i], properties[j]) >= k:
                    edge = True
                    graph[i].append(j)
                    graph[j].append(i)
            if not edge and i not in graph:
                graph[i].append(i)

        number_of_components = 0
        visited = [False]*len(properties)

        def dfs(node, visited):
            visited[node] = True
            for next_node in graph[node]:
                if visited[next_node] == False:
                    dfs(next_node, visited)

        for i in range(len(properties)):
            if visited[i] == False:
                dfs(i, visited)
                number_of_components += 1

        return number_of_components


s = Solution()
print(s.numberOfComponents(
    [[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]], 1))
print(s.numberOfComponents([[1, 2, 3], [2, 3, 4], [4, 3, 5]], 2))
print(s.numberOfComponents([[1, 1], [1, 1]], 2))
print(s.numberOfComponents([[4, 3], [2, 5], [2, 1], [1, 2], [3, 2]], 1))
print(s.numberOfComponents([[4], [5], [4], [5]], 1))
