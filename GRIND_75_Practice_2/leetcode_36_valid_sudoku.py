class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            checker_row = set()
            checker_col = set()
            for j in range(9):
                value = ord(board[i][j]) - ord('0')
                if value in checker_row:
                    return False
                if 0 <= value <= 9:
                    checker_row.add(value)
                value = ord(board[j][i]) - ord('0')
                if value in checker_col:
                    return False
                if 0 <= value <= 9:
                    checker_col.add(value)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                checker_box = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        value = ord(board[k][l]) - ord('0')
                        if value in checker_box:
                            return False
                        if 0 <= value <= 9:
                            checker_box.add(value)

        return True


s = Solution()
print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
