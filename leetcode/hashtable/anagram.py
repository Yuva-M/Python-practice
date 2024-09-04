from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_maps = defaultdict(list)
        result = []
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_maps[sorted_s].append(s)
        
        for i in anagram_maps.values():
            result.append(i)
        
        return result   