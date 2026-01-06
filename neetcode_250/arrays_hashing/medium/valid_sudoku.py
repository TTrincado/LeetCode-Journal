class Solution:
    """
    First approach, Multipass, we validate the Sudoku constraints one by one. 
    1. Iterate rows to check for duplicates using a HashSet.
    2. Iterate columns to check for duplicates.
    3. Iterate 3x3 sub-boxes using nested loops.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Validate Rows
        for i in range(9):
            seen = set()
            for k in range(9):
                val = board[i][k]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # 2. Validate Columns
        for k in range(9):
            seen = set()
            for i in range(9):
                val = board[i][k]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # 3. Validate 3x3 Sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        cell = board[r][c]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)
        return True

class Solution:
    """
    Approach 2: Single-Pass with Hash Map.
    
    Time Complexity: O(N^2)
    Space Complexity: O(N^2) to store the sets of seen numbers.
    
    Logic:
    We maintain three HashMaps (Dictionaries of Sets) simultaneously:
    - rows[r]: Tracks numbers seen in row 'r'.
    - cols[c]: Tracks numbers seen in col 'c'.
    - squares[(r//3, c//3)]: Tracks numbers seen in the box at grid coordinate (r//3, c//3).
    
    Key trick: Using a tuple (r // 3, c // 3) as a dictionary key to identify the 3x3 box.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # Key will be (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                # Check if the value exists in any of the 3 corresponding buckets
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # Add value to all 3 buckets simultaneously
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True