class Solution:
    """
    Logic:
    Instead of searching directly for the minimum, we search for the maximum element (the Pivot).
    In a rotated sorted array (e.g., [3, 4, 5, 1, 2]), the minimum is always 
    immediately after the maximum.
    
    1. We compare 'mid' against the rightmost element.
    2. If nums[mid] > right: We are in the left sorted portion (values are large). 
       The drop-off (minimum) must be to the right. We store this mid as a candidate for MAX.
    3. If nums[mid] < right: We are in the right sorted portion (values are small).
       The maximum must be to the left.
    
    Result: The minimum is at index 'max_index + 1'.
    
    Time Complexity: O(log N).
    Space Complexity: O(1).
    """
    def findMin(self, nums: list[int]) -> int:
        pos = (nums[len(nums) - 1], len(nums)) # max, index upper bound
        l, r = 0, len(nums)

        while l <= r:
            mid = l + (r-l)//2
            num = nums[mid]

            if num > pos[0]: # we're in rotated nums section, there can still be a bigger number
                pos = (num, mid) # new max
                l = mid + 1
            else: # the number is smaller, we keep looking to the left to find the rotated section
                r = mid - 1

        if pos[1] == len(nums):
            return nums[0]
        else:
            return nums[pos[1] + 1]
        
    def findMin(arr):
        """
        Same but more elegant solution.
        """
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                r = mid
        return l