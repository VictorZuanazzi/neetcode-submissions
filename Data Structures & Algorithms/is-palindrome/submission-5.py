class Solution:
    def isPalindrome(self, s: str) -> bool:

        def is_allowed(c):
            return ("a" <= c <= "z") or ("0" <= c <= "9")
        
        s = s.lower()
        f_index = 0
        b_index = len(s) - 1
        while f_index < b_index:

            f_char = s[f_index]
            if not is_allowed(f_char):
                f_index += 1
                continue

            b_char = s[b_index]
            if not is_allowed(b_char):
                b_index -= 1
                continue
            
            if f_char != b_char:
                return False

            f_index +=1
            b_index -= 1
        
        return True