class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)

        if len(nums_s) < 2:
            return len(nums_s)

        starters = set()
        enders = set()
        for n in nums_s:
            if ((n + 1) in nums_s) and ((n - 1) not in nums_s):
                starters.add(n)
            elif ((n - 1) in nums_s) and ((n + 1) not in nums_s):
                enders.add(n)

        if len(starters) == 0:
            return 1

        lenghs = []
        max_end = max(enders)
        for s in starters:
            lenghs.append(0)
            for i in range(s, max_end + 1):
                if i in nums_s:
                    lenghs[-1] += 1
                else:
                    break

        return max(lenghs) 
        