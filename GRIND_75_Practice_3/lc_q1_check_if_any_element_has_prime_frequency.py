class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                     37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        nums_hash_map = {}

        for num in nums:
            if num in nums_hash_map:
                nums_hash_map[num] += 1
            else:
                nums_hash_map[num] = 1

        for num in nums_hash_map:
            if nums_hash_map[num] in prime_set:
                return True
        return False


s = Solution()
print(s.checkPrimeFrequency([1, 2, 3, 4, 5, 4]))
