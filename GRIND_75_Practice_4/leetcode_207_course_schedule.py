from collections import deque, defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0]*numCourses
        dependency_map = defaultdict(list)
        courses_taken = 0
        q = deque([])

        for course, prereq in prerequisites:
            dependency_map[prereq].append(course)
            degrees[course] += 1

        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)

        while q:
            current_course = q.popleft()
            courses_taken += 1
            for course in dependency_map[current_course]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    q.append(course)
        return courses_taken == numCourses


s = Solution()
print(s.canFinish(3, [[1, 0], [2, 0], [0, 2]]))
