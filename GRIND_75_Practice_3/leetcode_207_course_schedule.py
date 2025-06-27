from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_map = defaultdict(list)
        dependency_degree = [0]*numCourses

        for course, prereq in prerequisites:
            course_map[prereq].append(course)
            dependency_degree[course] += 1

        queue = deque([i for i in range(numCourses)
                      if dependency_degree[i] == 0])

        courses_taken = 0

        while queue:
            course = queue.popleft()
            courses_taken += 1
            for c in course_map[course]:
                dependency_degree[c] -= 1
                if dependency_degree[c] == 0:
                    queue.append(c)
        return courses_taken == numCourses


s = Solution()
print(s.canFinish(5, [[1, 0], [0, 1], [3, 0], [4, 0]]))
