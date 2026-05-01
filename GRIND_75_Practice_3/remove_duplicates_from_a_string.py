class Solution():
    def removeDup(self, s):
        st_l = "".join(s.split(" "))
        output = set()
        res = ""

        for c in st_l:
            if c not in output:
                res += c
                output.add(c)
        return res


s = Solution()
print(s.removeDup("aman"))
