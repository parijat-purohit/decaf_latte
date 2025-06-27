# Time Complexity: O(3^N) (Worst Case: 4^N)
# Space Complexity: O(3^N) (Worst Case: 4^N)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_int_map = {"2": "abc", "3": "def",
                       "4": "ghi", "5": "jkl", "6": "mno",
                       "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if digits == "":
            return []
        output = [""]
        for d in digits:
            temp = []
            for c in dig_int_map[d]:
                for s in output:
                    temp.append(s+c)
            output = temp
        return output


s = Solution()
print(s.letterCombinations("23"))
