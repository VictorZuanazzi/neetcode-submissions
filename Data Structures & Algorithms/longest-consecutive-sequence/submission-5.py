class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # O(nlogn)
        # nums = sorted(nums)

        # max_strides = [0]
        # last_n = nums[0]
        # for n in nums[1:]:
        #     if (last_n + 1 == n) or (last_n == n):
        #         max_strides[-1] += 1
        #     else:
        #         max_strides.append(0)
        #     last_n = n

        # O(K) where K = max(nums)
        # min_n = min(nums)
        # max_n = max(nums)
        # nums = set(nums)
        # max_strides = [0]
        # for i in range(min_n, max_n + 1):
        #     if i in nums:
        #         max_strides[-1] += 1
        #     else:
        #         max_strides.append(0)

        # return max(max_strides)
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
        