class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)

        if len(nums_s) < 2:
            return len(nums_s)

        longest_sequence = 1
        for n in nums_s:
            if ((n + 1) in nums_s) and ((n - 1) not in nums_s):
                lengh_ = 1
                while (n + lengh_) in nums_s:
                    lengh_ += 1

                longest_sequence = max(longest_sequence, lengh_)

        return longest_sequence
        