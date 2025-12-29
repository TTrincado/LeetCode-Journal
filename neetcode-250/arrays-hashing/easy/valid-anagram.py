from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Strategy: Create a hash map that tracks frequency.
        charmap = defaultdict(int)

        for letter in s:
            charmap[letter] += 1

        for letter in t:
            charmap[letter] -= 1
            # Early exit: If count drops below zero, 't' has extra chars.
            if charmap[letter] < 0:
                return False

        # Time: O(n) - We iterate through both strings once.
        # Space: O(1) - The map size stays within 26 characters (a-z).
        return True
