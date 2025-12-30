from collections import defaultdict

class Solution:
    """
    Hash map approach. Uses O(N) space to track seen elements.
    Note: Not space-optimal since it doesn't take advantage of the array
    being pre-sorted.
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        seen = defaultdict(lambda: -1)
        k = 0
        for index, num in enumerate(nums):
            if seen[num] == -1:
                nums[k] = num
                seen[num] = 1
                k += 1
        return k
    
class Solution2:
    """
    Two-Pointer approach. Since the array is sorted, we can compare 
    neighbors to filter duplicates in-place with O(1) space.
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i