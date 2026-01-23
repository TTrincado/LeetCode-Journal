class Solution:
    """
    Approach: Binary Search (Virtual Flattening).

    Logic: We can just flatten the matrix to get a sorted 1D array of size M * N
    by using math to map a 1D index to 2D coordinates on the fly.

    Time Complexity: O(log(m * n)).
    Space Complexity: O(1).
    """
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix: return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            row = mid // COLS
            col = mid % COLS
            
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False