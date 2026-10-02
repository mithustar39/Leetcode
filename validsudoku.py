class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #check duplicates in row colums and 3x3
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):

                position = board[r][c]

                if position == ".":
                    continue
                box_position = (r//3)*3 + c//3

                if (position in rows[r]) or (position in cols[c]) or (position in boxes[box_position]):
                    return False
                
                rows[r].add(position)
                cols[c].add(position)
                boxes[box_position].add(position)
        return True

        
