class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0

        # Two pointers (naive):
        # l, r = 0, 1
        # temp_set = set(s[l])
        # max_length = 1
        # while r < len(s):
        #     if s[r] not in temp_set:
        #         temp_set.add(s[r])
        #         r +=1
        #     else:
        #         l += 1
        #         r = l + 1
        #         temp_set = set(s[l])
        #     max_length = max(max_length, len(temp_set))

        # two pointers (hits)
        l, r = 0, 1
        temp_set = set(s[l])
        max_length = 1
        while r < len(s):
            if s[r] not in temp_set:
                temp_set.add(s[r])
                r +=1
            else:
                temp_set.remove(s[l])
                l += 1

            max_length = max(max_length, len(temp_set))
            
        return max_length

            

        