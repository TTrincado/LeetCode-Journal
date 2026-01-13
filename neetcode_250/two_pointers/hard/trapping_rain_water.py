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
    
class Solution:
    """
    Approach: Two Pointers.
    
    Core Logic:
    Instead of pre-computing 'max_left' and 'max_right' arrays (which takes O(N) space),
    we use two pointers that move inward.
    
    The Key Insight:
    The amount of water at any index is determined by the shorter of the two walls:
    Water = min(max_L, max_R) - height[i].
    
    By maintaining 'max_left' and 'max_right' variables and always moving the pointer 
    on the shorter side, we guarantee that the current side is the limiting factor.
    We don't need to know the exact height of the other side, only that it is taller.

    And so, we go forward moving the pointers as we calculate the water trapped in the ith position,
    where we move the smallest pointer (if they are equal, it doesnt matter which one we move, I chose left)
    and check if we have a new max_direction.

    Time Complexity: O(N) - We process each element exactly once.
    Space Complexity: O(1) - Only constant extra variables used.
    """
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        res = 0

        while l < r:
            if max_left <= max_right: 
                l += 1
                max_left = max(max_left, height[l])
    
                # Because we updated max_left first, (max_left - height[l]) is guaranteed >= 0.
                res += max_left - height[l]

            else:
                r -= 1
                max_right = max(max_right, height[r])
                
                res += max_right - height[r]

        return res