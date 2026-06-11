class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_s = set(nums)
        if len(nums_s) < 2:
            return len(nums_s)

        starters = set()
        for n in nums_s:
            if ((n + 1) in nums_s) and ((n - 1) not in nums_s):
                starters.add(n)

        if len(starters) == 0:
            return 1

        lenghs = []
        for s in starters:
            lenghs.append(0)
            for i in range(s, max(nums) + 1):
                if i in nums_s:
                    lenghs[-1] += 1
                else:
                    break

        return max(lenghs) 
        