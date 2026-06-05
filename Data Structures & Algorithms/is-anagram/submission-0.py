class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def _build_dict(s):
            dict_s = {}
            for c in s:
                dict_s[c] = 1 + dict_s.get(c, 0)
            return dict_s
        
        dict_s = _build_dict(s)
        dict_t = _build_dict(t)

        for char, times in dict_s.items():
            if dict_t.get(char, 0) != times:
                return False
        
        return True
