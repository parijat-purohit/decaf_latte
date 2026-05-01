class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
