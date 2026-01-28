class Solution:
    """
    Approach 1: Single Pass 

    Logic:
    We iterate through the prices while keeping track of the lowest price seen so far.
    At every day we calculate what would be the profit if I sell today.
    
    
    Time Complexity: O(N).
    Space Complexity: O(1).
    """
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit

class Solution2:
    """
    Approach 2: Two Pointers / Sliding Window

    Logic:
    Conceptually identical but uses explicit pointers.
    - 'l' (Left) points to the Buying day.
    - 'r' (Right) points to the Selling day.
    
    If prices[r] < prices[l], it means we found a cheaper buying price. 
    We reset the old window and move 'l' to 'r'.

    Time Complexity: O(N).
    Space Complexity: O(1).
    """
    def maxProfit_alternative(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP