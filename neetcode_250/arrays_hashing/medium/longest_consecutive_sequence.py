class Solution:
    def longestConsecutiveQuadratic(self, nums: list[int]) -> int:
        """
        Attempt 1: Quadratic Approach (Failed in time complexity requirements).

        The logic tries to identify candidates that 'have a successor' (num + 1).

        CRITICAL FLAW:
        This condition selects ANY number that is not the end of a sequence.
        Example: [1, 2, 3, 4, 5]
        - 1 has 2 -> Candidate. Loop runs for 2, 3, 4, 5.
        - 2 has 3 -> Candidate. Loop runs for 3, 4, 5.
        - ...

        This results in redundant computations, leading to O(N^2) complexity.
        """
        if len(nums) == 0:
            return 0

        hashset = set(nums)
        candidates = []

        for num in nums:
            if num + 1 in hashset:
                candidates.append(num)

        longest = 1
        count = 1

        for candidate in candidates:
            while True:
                if candidate + count in hashset:
                    count += 1
                else:
                    break
            if count > longest:
                longest = count

            count = 1

        return longest

    def longestConsecutiveSet(self, nums: list[int]) -> int:
        """
        Approach 2: HashSet with Intelligent Filtering.

        Time Complexity: O(N)
        Space Complexity: O(N)

        Logic:
        1. Store all numbers in a Set for O(1) lookups.
        2. Iterate through the set.
        3. Check if 'num' is the beginning of a sequence by verifying if (num - 1) exists.

        This ensures the inner while loop runs exactly once per sequence, 
        making the total complexity linear.
        """
        hashset = set(nums)
        longest = 0

        for num in nums:
            # Identify beginning of sequence
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1

                longest = max(length, longest)

        return longest
