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

        def dfs(row, col, ind):
            if ind == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[ind] or (row, col) in path):
                return False
            path.add((row, col))
            if (dfs(row+1, col, ind+1) or dfs(row-1, col, ind+1) or dfs(row, col+1, ind+1) or dfs(row, col-1, ind+1)):
                return True
            path.remove((row, col))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


s = Solution()
print(s.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
