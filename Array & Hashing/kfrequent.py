import operator
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sort_freq = sorted(freq.items(), key=operator.itemgetter(1, 0), reverse=True)
        sliced = sort_freq[:k]
        return [num for num, count in sliced]



           

        
           
            

