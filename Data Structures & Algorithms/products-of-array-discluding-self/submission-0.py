class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixes = []
        prod = 1
        for n in nums:
            prefixes.append(prod)
            prod *= n

        suffices = []
        prod = 1
        for n in nums[::-1]:
            suffices.append(prod)
            prod *= n
        
        prods = []
        for p, s in zip(prefixes, suffices[::-1]):
            prods.append(p * s)

        return prods