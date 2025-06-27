"""
It's a bit hard to remember the exact algorithm to find
the next permutation. So I am just writing plain pseudo
algorithm for my own ease.
Step 1: Find the pivot point while traversing backwards that satisfies
        nums[i] < nums[i+1]
Step 2: Now, we would again traverse backwards and swap only once if
        nums[pivot] < nums[i]
Step 3: Finally, we would return the list after reverse(nums[pivot+1:])

If there is no such pivot point, then reverse the entire list and return it.

Simple!
Time Complexity: O(N)
Space Complexity: O(1)
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        id = None
        if len(nums) == 1:
            return nums

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                id = i
                break

        if id is None:
            nums.reverse()
            return

        for j in range(len(nums)-1, -1, -1):
            if nums[id] < nums[j]:
                nums[id], nums[j] = nums[j], nums[id]
                break

        nums[id+1:] = reversed(nums[id+1:])


s = Solution()
print(s.nextPermutation([4, 3, 2, 1]))
print(s.nextPermutation([1, 2, 4, 3]))  # It should return [1, 3, 2, 4]
print(s.nextPermutation([1, 3, 2]))
