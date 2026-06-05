class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        # Bucket Sort
        max_freq = max(freq_map.values())
        freq_arr = [[] for i in range(max_freq+1)]

        for n, freq in freq_map.items():
            freq_arr[freq].append(n)

        # Retrieve the top k in reverse freq order
        top_k = []
        for freqs in freq_arr[::-1]:
            top_k.extend(freqs)
            if len(top_k) >= k:
                return top_k

        return top_k



