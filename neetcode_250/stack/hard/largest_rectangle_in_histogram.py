class Solution:
    """
    Approach: Dynamic Programming / Two Arrays (Left & Right Limits).
    
    Logic:
    Instead of using a Monotonic Stack to find boundaries in a single pass like the solution provided by NC suggested, 
    it made more sense to me if we pre-computed the 'limit' for each bar in two separate passes.
    
    1. 'left_limit[i]': The index of the first bar to the LEFT that is smaller than height[i].
    2. 'right_limit[i]': The index of the first bar to the RIGHT that is smaller than height[i].
    
    The width of the rectangle for bar 'i' is determined by these boundaries:
    Width = (right_limit - left_limit - 1)
    
    To calculate left_limit and right_limit in O(N), we use a 'jump' strategy. If neighbor 'p' is taller than current 'i', 
    we don't scan 'p's neighbors one by one. We jump directly to 'p's known limit:
    p = left_limit[p]. This ensures each index is processed constant times on average.

    Time Complexity: O(N) - technically O(3N) due to three passes, but simplifies to O(N). The Monotonic Stack one does compute in
    just O(N), but the difference is virtually irrelevant for time complexities.
    Space Complexity: O(N) - Two auxiliary arrays of size N.
    """
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        if n == 0: return 0
        
        left_limit = [0] * n 
        right_limit = [0] * n 
        
        left_limit[0] = -1 # Virtual boundary
        for i in range(1, n):
            p = i - 1
            
            # DP Logic: Jump over bars that are taller or equal
            while p >= 0 and heights[p] >= heights[i]:
                p = left_limit[p]
            
            left_limit[i] = p

        right_limit[n-1] = n # Virtual boundary
        for i in range(n - 2, -1, -1):
            p = i + 1
            
            # DP Logic: Jump over bars that are taller or equal
            while p < n and heights[p] >= heights[i]:
                p = right_limit[p]
            
            right_limit[i] = p
            
        max_area = 0
        for i in range(n):
            width = right_limit[i] - left_limit[i] - 1
            area = heights[i] * width
            if area > max_area:
                max_area = area
            
        return max_area