import re

class Solution:
    """
    Pretty straight forward regex approach
    """
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return clean_s == clean_s[::-1]

class Solution:
    """
    Two Pointers approach, we skip non alfanumeric letters and check if both letters from both pointers coincide.

    Time complexity: O(n) - We iterate through the string once.
    Space complexity: O(1) - Pointers storage is constant.
    """
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
            