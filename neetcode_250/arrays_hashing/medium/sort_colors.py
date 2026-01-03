class Solution:
    """
    Here I learned something about the enumerate function.
    The value is storaged as a local variable and if modified, it won't modify the
    original list. For example, doing value -= 1 just changes the temporal variable value,
    whilst count[position] -= 1 would actually change the list.

    Also, this made it luckily work. If we tried count[position] -= 1 instead of the value -= 1, the code
    would break as we would be modifying a list in which we are iterating. Either go for a "for i in range(3)"
    since the length is known, or leave the count list intact and modify the temporal value.

    Both are O(n) time and O(1) space complexities, but you could argue in the first solution an aditional variable
    is used.
    """

    def sortColorsOwnSolution(self, nums: list[int]) -> None:
        """
        O
        """
        count = [0] * 3

        for num in nums:
            count[num] += 1

        nums_index = 0
        for position, value in enumerate(count):
            while value:
                value -= 1  # <- Local variable
                nums[nums_index] = position
                nums_index += 1

    def sortColorsStandardSolution(self, nums: list[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

    def sortColorsThreePointers(self, nums: list[int]) -> None:
        """
        Another (more) clever way to solve the problem.
        Originally known as the Dutch National Flag problem (Dijkstra), uses three pointers to 
        partition the array in a single pass O(N) with O(1) space.

        - "l" (left): Tracks the boundary for 0s. All elements before "l" are 0.
        - "r" (right): Tracks the boundary for 2s. All elements after "r" are 2.
        - "i": The current element iterator.

        Logic:
        1. If 0: Swap with "l" and advance both "l" and "i". We know the swapped value is safe.
        2. If 1: Just advance "i".
        3. If 2: Swap with "r" and shrink "r". CRITICAL: We do NOT advance "i" (handled by i-=1)
           because the value swapped from "r" is unknown and must be re-evaluated.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                # Compensate the i+=1 below to stay in the same position
                i -= 1
            i += 1
