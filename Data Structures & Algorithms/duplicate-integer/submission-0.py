class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        mem = {}
        for num in nums:
            if num in mem:
                mem[num] = mem[num] + 1
            else:
                mem[num] = 1
            
            if mem[num] == 2:
                return True

        return False
            