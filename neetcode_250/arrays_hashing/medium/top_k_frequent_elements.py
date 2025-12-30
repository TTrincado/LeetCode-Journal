from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums) # O(n)
        top_k_items = counter.most_common(k) # O(nlog(k))
        return [item[0] for item in top_k_items]
        
        # Time complexity: O(nlog(k))
        # Space complexity: O(n)

        # Another solution could be done with a frequency table, which would be
        # O(n) in time and O(n) in space.