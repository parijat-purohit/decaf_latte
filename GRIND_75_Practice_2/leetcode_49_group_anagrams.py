class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        st_dict = {}
        output = []

        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st in st_dict:
                output[st_dict[sorted_st]].append(st)
            else:
                st_dict[sorted_st] = len(output)
                output.append([st])
        return output


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
