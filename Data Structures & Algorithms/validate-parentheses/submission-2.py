class Solution:

    @staticmethod
    def _is_pair(a, b):
            map_pairs = {
                "(": ")", "[": "]", "{": "}"
                }
            
            return map_pairs.get(a, "") == b


    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        
        def _is_opener(c):
            return c in "({["
        
        def _is_closer(c):
            return c in "}])"

        
        last_open = []
        for r, c in enumerate(s):
            if _is_opener(c):
                last_open.append(c)
            elif _is_closer(c):
                if (len(last_open) == 0) or (not self._is_pair(last_open[-1], c)):
                    return False
                else :
                    _ = last_open.pop(-1)


        return len(last_open) == 0






        