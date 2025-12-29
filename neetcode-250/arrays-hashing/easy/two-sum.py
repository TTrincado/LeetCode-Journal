class Solution:
    '''
    num1 + num2 = target
    num2 = target - num1 -> complement
    To extract num2 we need to calculate it for each index and save all num1 seen.
    '''

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Strategy: One-pass hash table that stores {value: index} of numbers we have seen so far.
        """
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i

        # Time: O(n) - We traverse the list containing n elements once.
        # Space: O(n) - The extra space required depends on the number of items stored in the hash table.
