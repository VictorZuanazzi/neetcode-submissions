import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = set(string.ascii_letters + string.digits)
        s_ = [c for c in s.lower() if c in allowed]
        return s_ == s_[::-1]