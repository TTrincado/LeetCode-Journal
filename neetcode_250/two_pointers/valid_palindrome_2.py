class Solution:
    """
    Uses the same logic used in valid palindrome 1, but since we have 
    to check inside an if the time complexity rises to O(n^2).
    """

    def isPalindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True

        for i in range in len(s):
            poss = s[:i] + s[i + 1:]
            if self.isPalindrome(poss):
                return True

        return False


class Solution2:
    """
    Strategy: Check for a missmatch and check if forgiving that letter produces a palindrome.
    """

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                skip_i = s[i+1: j+1]
                skip_j = s[i: j]

                return (skip_i == skip_i[::-1]) or (skip_j == skip_j[::-1])

            i += 1
            j -= 1

        return True
