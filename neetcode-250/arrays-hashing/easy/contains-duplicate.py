class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Sets remove duplicates automatically.
        # If the set length is different from the list length, duplicates existed.
        # Time: O(n) | Space: O(n).
        return not (len(nums) == len(set(nums)))
