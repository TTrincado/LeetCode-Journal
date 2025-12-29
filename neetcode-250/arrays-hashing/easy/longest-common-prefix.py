class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''
        Strategy: Horizontal Scanning (Kind of brute forced, first approach)
        '''
        # Take the first word as a base and compare it against the next one,
        # updating the common prefix as we go.
        if len(strs) == 1:
            return strs[0]

        base1 = strs[0]
        base2 = strs[1]
        ans = ""

        # Get first longest prefix between the first 2 words
        # Shortest word dictates the initial loop length
        for i in range(min(len(base1), len(base2))):
            w1_letter = base1[i]
            w2_letter = base2[i]
            if w1_letter == w2_letter:
                ans += w1_letter
            else:
                break

        # Compare the prefix with the rest of the words, one by one.
        for i in range(2, len(strs)):
            word = strs[i]
            for k in range(len(word)):
                # Compare ans until we run it all
                if k <= len(ans) - 1:
                    letter = word[k]
                    ans_letter = ans[k]
                    if letter == ans_letter:
                        if k + 1 == len(word):
                            ans = ans[0:k+1]
                        continue
                    else:
                        # Cut ans to how far we made it
                        ans = ans[0:k]
                        break

        return ans

    # Time Complexity: O(S) - Worst case, checks every character.
    # Space Complexity: O(1)

# Note that it could be optimized. ans is always being processed to the word's
# length despite the possibility of ans being shorter.

# LC provides a solution taking this into account,
# as well as a more elegant execution.
    def longestCommonPrefixV2(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

# Finally, there is the "Vertical Scanning" approach, in which we
# iterate and compare through the letters of each word at once.

# Despite being also O(S), it ends quicker when the list contains shorter words
# after the first word.
    def longestCommonPrefixV3(self, strs: list[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
