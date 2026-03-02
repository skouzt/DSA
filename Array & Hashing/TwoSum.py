class Solution:
    def twoSum(self, nums, target: int):
        hash_set = dict()
        for i, val in enumerate(nums):
            b = target - val
            if b in hash_set:  
                return hash_set[b],i
            else:
                hash_set[val] = i
        
           