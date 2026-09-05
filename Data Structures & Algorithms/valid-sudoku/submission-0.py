class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            row = set()
            for j in range(9):
                curr = board[i][j]
                if curr in row:
                    return False
                elif curr == ".":
                    continue
                else:
                    row.add(curr)
        
        # Check columns
        for j in range(9):
            col = set()
            for i in range(9):
                curr = board[i][j]
                if curr in col:
                    return False
                elif curr == ".":
                    continue
                else:
                    col.add(curr)
        
        # Check 3 x 3 squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                sq = set()
                for i in range(3):
                    for j in range(3):
                        curr = board[row + i][col + j]
                        if curr in sq:
                            return False
                        elif curr == ".":
                            continue
                        else:
                            sq.add(curr)
        
        return True
            
        