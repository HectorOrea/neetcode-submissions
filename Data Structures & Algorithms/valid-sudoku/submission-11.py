class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make rows, make columns, make squares, check them each
        def strip_blanks(piece : List[str]) -> List[int]:
            res = []
            for c in piece:
                if c.isdigit():
                    res.append(int(c))
            return res

        raw_rows = [board[:][i] for i in range(9)]
        cleaned_rows = [strip_blanks(row) for row in raw_rows]
        for row in cleaned_rows:
            s = set(row)
            if len(s) != len(row):
                return False
        
        raw_cols = [[row[j] for row in raw_rows] for j in range(9)]
        cleaned_cols = [strip_blanks(col) for col in raw_cols]
        for col in cleaned_cols:
            s = set(col)
            if len(s) != len(col):
                return False
        
        square_index_sets = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
        raw_squares = []
        for row_idx in square_index_sets:
            for col_idx in square_index_sets:
                cur_square = []
                for r in row_idx:
                    for c in col_idx:
                        cur_square.append(board[r][c])
                raw_squares.append(cur_square)
        
        cleaned_squares = [strip_blanks(square) for square in raw_squares]
        for square in cleaned_squares:
            s = set(square)
            if len(s) != len(square):
                return False
        
        return True

        