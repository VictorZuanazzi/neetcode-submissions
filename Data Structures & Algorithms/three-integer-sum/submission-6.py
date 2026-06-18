class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # virando o loop do aveco
        triplets = set()
        nums = sorted(nums)
        for right, low in enumerate(nums):
            
            mid = right + 1
            left = len(nums) - 1

            while mid < left:
                sum_ = low + nums[mid] + nums[left]
                if sum_ == 0:
                    triplets.add((low, nums[mid], nums[left]))
                if sum_ >= 0:
                    left -= 1
                elif sum_ < 0:
                    mid += 1

        return list(triplets)
