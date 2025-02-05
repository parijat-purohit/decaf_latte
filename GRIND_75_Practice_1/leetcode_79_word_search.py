class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols
                    or word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            result = (dfs(r+1, c, i+1) or
                      dfs(r-1, c, i+1) or
                      dfs(r, c+1, i+1) or
                      dfs(r, c-1, i+1))
            path.remove((r, c))
            return result

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
      ["A", "D", "E", "E"]], "ABCCED"))
