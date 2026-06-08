class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [0, 0]
        
        i = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [0, 0]
            


#                 i=j
# num = [5, 6, 3, 4]
# target = 10
#
