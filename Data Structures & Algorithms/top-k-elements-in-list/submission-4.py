class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        max_freq = 0
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
            max_freq = max(max_freq, freq_map[n])

        # Bucket Sort
        # max_freq = max(freq_map.values())
        freq_arr = [None] * (max_freq + 1)
        for n, freq in freq_map.items():
            if freq_arr[freq] is None:
                freq_arr[freq] = [n]
            else:
                freq_arr[freq].append(n)

        top_k = []
        for freqs in freq_arr[::-1]:
            if freqs is not None:
                top_k.extend(freqs)
            if len(top_k) >= k:
                return top_k

        return top_k



