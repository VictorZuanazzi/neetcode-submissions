import string
from copy import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        abc = {k: 0 for i, k in enumerate(string.ascii_lowercase)}

        def _build_descriptor(w):
            descriptor = copy(abc)
            for c in w:
                descriptor[c] += 1
            return str(list(descriptor.values()))

        desc_map = {}
        for word in strs:
            word_d = _build_descriptor(word)
            desc_map[word_d] = desc_map.get(word_d, []) + [word]

        return list(desc_map.values())
