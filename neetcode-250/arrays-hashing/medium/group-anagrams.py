from collections import defaultdict


class Solution:
    """
    Strategy: Sort the words and create a hash map -> { sorted_word: [word1, word2, ...]}
    """

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        First approach
        """
        hashmap = defaultdict(list)
        ans = []

        # Strategy: sort and save the sorted word
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)

        for value in hashmap.values():
            ans.append(value)

        return ans

        # O(n · k log k), since we sort each word. It can be optimized via counting the frequency of each letter.
        # Also, ans was redundant -> return list(hashmap.values())

    def groupAnagramsV2(self, strs: list[str]) -> list[list[str]]:
        """
        Optimized solution. Counts the frequency of letters and stores it in a hashmap.
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
