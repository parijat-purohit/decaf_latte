from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        dependency_map = defaultdict(list)
        courses_taken = 0

        for course, prereq in prerequisites:
            dependency_map[prereq].append(course)
            degrees[course] += 1

        queue = deque(i for i in range(numCourses) if degrees[i] == 0)

        while (queue):
            current_course = queue.popleft()
            courses_taken += 1
            for course in dependency_map[current_course]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    queue.append(course)

        return courses_taken == numCourses


s = Solution()
print(s.canFinish(3, [[1, 0], [2, 0], [2, 1]]))
