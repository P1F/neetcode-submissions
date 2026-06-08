class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] = freq[c] + 1
            else:
                freq[c] = 1

        for c in t:
            if c in freq:
                freq[c] = freq[c] - 1
            else:
                return False

        for k in freq:
            if freq[k] != 0:
                return False

        return True