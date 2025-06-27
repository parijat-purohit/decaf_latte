class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_ch_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                      "7": "pqrs", "8": "tuv", "9": "wxyz"}

        output = [""]

        for d in digits:
            temp = []
            chars = dig_ch_map[d]
            for ch in chars:
                for o in output:
                    temp.append(o+ch)
            output = temp
        return output


s = Solution()
print(s.letterCombinations("34"))
