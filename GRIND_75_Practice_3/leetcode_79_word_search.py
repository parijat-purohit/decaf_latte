class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        path = set([])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in path and board[r][c] == word[i]:
                path.add((r, c))
                res = (dfs(r-1, c, i+1) or
                       dfs(r+1, c, i+1) or
                       dfs(r, c-1, i+1) or
                       dfs(r, c+1, i+1))
                path.remove((r, c))
                return res
            else:
                return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
      ["A", "D", "E", "E"]], "ABCB"))
print(s.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
