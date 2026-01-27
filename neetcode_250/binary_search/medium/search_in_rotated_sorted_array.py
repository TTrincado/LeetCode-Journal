class Solution:
    """
    Logic:
    Instead of handling complex conditions in a single pass, we break the problem 
    into two standard sub-problems:
    
    1. Find the Pivot Index: Locate the minimum element index. This tells us 
       where the rotation happened and divides the array into two sorted subarrays.
       - Left Subarray: [0 ... pivot-1] (Large values)
       - Right Subarray: [pivot ... n-1] (Small values)
       
    2. Select the Correct Side:
       - Check if 'target' falls within the range of the Right Subarray 
         (nums[pivot] <= target <= nums[-1]).
       - If yes, Binary Search on the Right.
       - If no, Binary Search on the Left.
       
    Time Complexity: O(log N) + O(log N) = O(log N).
    Space Complexity: O(1) (We use indices, we do NOT slice the array).
    """
    def search(self, nums: list[int], target: int) -> int:
        if not nums: return -1

        def findPivotIndex(arr):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + (r - l) // 2
                if arr[mid] > arr[-1]:
                    l = mid + 1
                else:
                    r = mid
            return l

        def binarySearch(arr, l, r, target):
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        pivot = findPivotIndex(nums)
        
        if nums[pivot] <= target <= nums[-1]:
            return binarySearch(nums, pivot, len(nums) - 1, target)
        else:
            return binarySearch(nums, 0, pivot - 1, target)

    """
    CRITICAL NOTE ON IMPLEMENTATION (mistake I initially made):
    
    Avoid using list slicing like 'binarySearch(nums[pivot:], target)'.
    
    This causes some issues with:
    1. Complexity: Slicing creates a copy of the list, which is O(N). 
       This destroys the logarithmic time complexity advantage.
    2. Index Mapping: Searching in a sliced copy returns the index relative to 
       the copy (e.g., 0), not the original list (e.g., 5).
    
    Always pass 'left' and 'right' boundary indices to keep it O(1) space.
    """