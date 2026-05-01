class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {"2": "abc", "3": "def",
                     "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs",
                     "8": "tuv", "9": "wxyz"}

        if len(digits) == 0:
            return []

        output = ['']
        for d in digits:
            chars = digit_map[d]
            temp = []
            for ch in chars:
                for o in output:
                    temp.append(o + ch)
            output = temp
        return output


s = Solution()
print(s.letterCombinations("23"))
