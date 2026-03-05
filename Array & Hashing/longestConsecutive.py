from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_num = set(nums)
        longest = 0
        for num in set_num:
            current = num
            length = 1 
            if num-1 not in set_num:
                while current+1 in set_num:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
            