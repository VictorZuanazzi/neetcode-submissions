class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {v:i for i, v in enumerate(nums)}

        for i, n1 in enumerate(nums):
            complement = target - n1
            if j := hmap.get(complement, False):
                if j == i:
                    continue
                return [i, j]
        