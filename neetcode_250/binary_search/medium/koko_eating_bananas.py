import math

class Solution:
    """
    Logic:
    1. Define the upper bound as the max possible k being max(piles) (In this way, 
    it takes len(piles) hours to eat all the bananas).
    2. Iterate from 1 ... max(piles) with binary search to find the optimum k.
    
    Time Complexity: O(N * log(M)) where N is piles length, M is max pile size.
    Space Complexity: O(1).
    """
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) 

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res