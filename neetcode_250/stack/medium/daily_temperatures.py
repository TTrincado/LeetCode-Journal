class Solution:
    """
    Approach: Monotonic Decreasing Stack.

    Logic:
    We need to find the distance to the next greater element.
    For this, we use a "Monotonic Stack" (stores values in a decreasing or increasing order) to store
    indices of days that haven't found a warmer day yet.

    1. Loop through each day (current_temp).
    2. Check Stack Top: current_temp > stack_top_temp?
        True: Warmer day -> Pop it, calculate distance (current_index - popped_index), update res array.
              We need to repeat while the stack is not empty and the condition holds for the new top of the stack.
        False: Check the next temperature and append the new "coldest" one to the top of the stack.

    Time Complexity: O(N). Each element is added to the stack once and popped at most once.
    Space Complexity: O(N). Worst case (decreasing array like [90, 80, 70]), stack holds all.
    """

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        # Stores pairs (temp, index) to calculate the index or to compare in the future
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()  # Here we dont need the temp, so we just ignore it
                # Current Day Index - Past Day Index
                res[stackInd] = i - stackInd

            stack.append((t, i))

        return res
