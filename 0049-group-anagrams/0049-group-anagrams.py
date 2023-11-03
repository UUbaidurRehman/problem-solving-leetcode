from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for sword in strs:
            sorted_word = ''.join(sorted(sword))
            anagrams[sorted_word].append(sword)
        return list(anagrams.values())
            