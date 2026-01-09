class Solution:
    """
    Approach: Sorting + Two Pointers, we fix one number and use two pointers to find the other two.
    
    Time Complexity: O(N^2) -> Sorting takes O(N log N), but the main loop runs N times, and the inner while loop runs O(N) times.
    Space Complexity: O(1) or O(N) depending on sorting implementation. sort() probably uses TimSort.
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            # If the current fixed number is positive, 
            # we can't sum to 0 because the array is sorted.
            if value > 0:
                break

            # Duplicate Check: if the value is the same as the previous number, we skip it.
            # (we already processed all triplets in the previous iteration)
            if index > 0 and value == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            
            while left < right:
                threeSum = value + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -= 1 # Sum too big
                elif threeSum < 0:
                    left += 1  # Sum too small
                else:
                    res.append([value, nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    # Duplicate Check:
                    # We only need to check one side (left) to avoid duplicate triplets.
                    # We slide 'left' forward as long as it points to the same number as before.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res