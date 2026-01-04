class Solution:
    """
    Solved using the Prefix & Suffix Product technique, the hint helped me.

    The core idea is that for any index 'i', the product of all elements except self 
    is equivalent to:
    (Product of all nums to the LEFT of i) * (Product of all nums to the RIGHT of i).

    Complexity:
    - Time: O(N) (We iterate through the list 3 times)
    - Space: O(N) (We use two extra arrays of size N)
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length

        # Calculate Prefix (Accumulate from Left)
        for i in range(1, length):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # Calculate Suffix (Accumulate from Right)
        for i in range(length - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        for i in range(length):
            nums[i] = prefix[i] * suffix[i]

        return nums
