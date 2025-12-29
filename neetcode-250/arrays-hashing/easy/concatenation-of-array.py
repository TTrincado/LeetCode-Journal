class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # The '*' operator creates a copy of the list n times.
        # Time: O(n) | Space: O(n)
        return nums * 2 

    def getConcatenationV2(self, nums: list[int]) -> list[int]:
        # Alternative approach: Directly join two lists together via +.
        # Time: O(n) | Space: O(n)
        return nums + nums