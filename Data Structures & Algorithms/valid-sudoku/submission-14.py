class Solution:
    from itertools import product
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Have dicts row, col, and square where row[i] is the set
        # of digits that appear in the i'th row
        # We will scan and add to the dicts as we go, and
        # if we ever come across the same digit twice 
        # we know the board is invalid

        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}

        square_indices = product([0, 1, 2], [0, 1, 2])
        squares = {(i, j) : set() for (i, j) in square_indices}
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                else:
                    n = int(c)
                    if n in rows[i]:
                        return False
                    rows[i].add(n)
                    if n in cols[j]:
                        return False
                    cols[j].add(n)
                    if n in squares[(i//3, j//3)]:
                        return False
                    squares[(i//3, j//3)].add(n)
        return True
                    
        