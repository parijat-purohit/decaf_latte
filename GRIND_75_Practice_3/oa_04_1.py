class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char_map = temp_char_map = [0]*26

        for ch in chars:
            char_map[ord(ch) - ord('a')] += 1

        counter, global_counter = 0, 0
        for word in words:
            temp_char_map = char_map[:]
            counter = 0

            for w in word:
                if temp_char_map[ord(w) - ord('a')] > 0:
                    temp_char_map[ord(w) - ord('a')] -= 1
                    counter += 1
                else:
                    counter = 0
                    break
            global_counter += counter

        return global_counter


s = Solution()
print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print(s.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
