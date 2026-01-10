class Solution:
    """
    The problem can be split in sub problems where we calculate how much water is in the current index.
    
    The water stored in the ith index can be calculated by looking for the tallest columns to the left
    and to the right, where the one with the smaller height will dictate how much water will be stored,
    and finally substracting the height of the current column.

    For this solution, we created 2 extra arrays that contains the biggest height seen from one index for
    both directions and then used it to calculate what was explained before.

    Note: This operation can sometimes result in a negative number, in which we round up to 0 since that just
    means no water is being stored.

    Time Complexity: O(N) - Single pass through the array.
    Space Complexity: O(N) - Array-size dependant space.
    """
    def trap(self, height: list[int]) -> int:
        n = len(height)
        max_left, max_right = [0] * n, [0] * n

        for i in range(1, n):
            max_left[i] = max(height[i - 1], max_left[i - 1])
        
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        water_trapped = 0
        for i in range(n):
            calc = min(max_left[i], max_right[i]) - height[i]
            if calc < 0:
                calc = 0
            water_trapped += calc

        return water_trapped