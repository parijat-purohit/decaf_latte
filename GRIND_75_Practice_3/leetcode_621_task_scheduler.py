class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        task_mapper = {}
        counter_with_max_frequency = 0
        for task in tasks:
            task_mapper[task] = task_mapper.get(task, 0) + 1
        frequency_max = max(task_mapper.values())
        counter_with_max_frequency = sum(
            1 for freq in task_mapper.values() if freq == frequency_max)
        return max(len(tasks), ((frequency_max - 1)*(n+1) + counter_with_max_frequency))


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
