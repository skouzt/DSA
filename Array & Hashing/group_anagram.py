from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str1 = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            str1[key].append(i) 
        return list(str1.values())