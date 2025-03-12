class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        unplaced_fruits = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    break
                if j == len(baskets)-1:
                    unplaced_fruits += 1
        return unplaced_fruits


s = Solution()
print(s.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))
print(s.numOfUnplacedFruits([3, 6, 1], [6, 4, 7]))
