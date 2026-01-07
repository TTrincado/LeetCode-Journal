class Solution:
    """
    Two-Pointer approach. Same logic as the merge algorithm in merge sort.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag = 0
        i, j = 0, 0
        res = ""
        while i < len(word1) and j < len(word2):
            if flag == 0:
                res += word1[i]
                i += 1
                flag += 1
            else:
                res += word2[j]
                j += 1
                flag -= 1

        res += word1[i:]
        res += word2[j:]

        return res
