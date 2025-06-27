class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
        print(dp)
        return dp[n]


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("catsandog", ["cats", "sand", "and", "cat"]))
