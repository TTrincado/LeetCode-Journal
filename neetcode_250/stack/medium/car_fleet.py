class Solution:
    """
    Approach: Monotonic Stack (Sorted by Position).

    Logic:

    1. We create a stack that will represent the times of arrival, the key idea here is that each new highest time of arrival represents
    a new fleet, so len(stack) will be the number of car fleets.

    2. We pair positions and speeds and sort them by position (descending).

    This allows us to process cars from the one closest to the target, and since the cars can't
    pass each other, this will be the "order of arrival".

    3. We calculate the 'arrival time' for each car: (target - pos) / speed.

    4. We process and check for the stack:
       - If the next car arrives faster, it catches up and merges into that fleet, so we discard it via popping.

       - If a car arrives slower (larger time), it becomes the leader of a new fleet. We keep it in the stack.

    Time Complexity: O(N log N) due to sorting.
    Space Complexity: O(N) to store the pairs and the stack.
    """

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        stack = []

        for position, speed in sorted(pairs, key=lambda pairs: pairs[0], reverse=True):
            time = (target - position) / speed
            stack.append(time)
            if len(stack) > 1:
                if stack[-1] > stack[-2]:
                    continue
                else:
                    stack.pop()

        return len(stack)

    """
    NOTE ON SYNTAX:
    In the line: sorted(pairs, key=lambda pairs: pairs[0], reverse=True)
    
    The 'key=lambda p: p[0]' is technically redundant because Python's default behavior 
    when sorting a list of tuples is to compare the first element (index 0) first.

    However, I keept it because it makes the code's intention easier to read.
    """
