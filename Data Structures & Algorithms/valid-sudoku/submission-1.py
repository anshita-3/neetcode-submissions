class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen=set()
            for num in row:
                if num=='.':
                    continue
                if num in seen:
                    return False
                seen.add(num) 
            
        for column in range(9):
            seen=set()
            for row in range(9):
                val=board[row][column]
                if val=='.':
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()
                for r in range(box_row,box_row+3):
                    for c in range(box_col,box_col+3):
                        val=board[r][c]
                        if val=='.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True