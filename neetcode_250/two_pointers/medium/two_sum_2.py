class Solution:
    """
    Conditions ask for the space complexity to be O(1). This means no Hashmap.
    By taking advantage of the list being sorted, we can compare from both ends to see
    if the target is bigger or smaller.
    """

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                # Sum is too big, move right pointer down
                right -= 1
            elif current_sum < target:
                # Sum is too small, move left pointer up
                left += 1
            else:
                return [left + 1, right + 1]  # 1-inexed array

        return []
