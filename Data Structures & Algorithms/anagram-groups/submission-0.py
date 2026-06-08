class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = {}
        first26primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        a_int = ord('a')

        for s in strs:
            signature = 1
            for c in s:
                idx = ord(c) - a_int
                signature = signature * first26primes[idx]
            if signature in signatures:
                signatures[signature].append(s)
            else:
                signatures[signature] = [s]

        res = []
        for k in signatures:
            res.append(signatures[k])
    
        return res