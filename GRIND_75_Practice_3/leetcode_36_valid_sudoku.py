class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set = set([])
        col_set = set([])
        sub_row_set = set([])

        for i in range(9):
            for j in range(9):
                ch_row = board[i][j]
                ch_col = board[j][i]
                if ch_row in row_set or ch_col in col_set:
                    return False
                if ch_row != '.':
                    row_set.add(ch_row)
                if ch_col != '.':
                    col_set.add(ch_col)
            row_set.clear()
            col_set.clear()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        ch = board[k+i][l+j]
                        if ch in sub_row_set:
                            return False
                        if ch != '.':
                            sub_row_set.add(ch)
                sub_row_set.clear()

        return True


s = Solution()
print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
