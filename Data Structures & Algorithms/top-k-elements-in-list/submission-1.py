class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        
        temp = []
        for key in freq:
            temp.append([freq[key], key])

        temp.sort(reverse=True)
        
        res = []
        for t in temp[:k]:
            res.append(t[1])

        return res

# space: O(n)
# time: O(nlogn)

