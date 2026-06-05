class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        top_k, top_f = [], []
        min_f = 0
        for n, freq in freq_map.items():
            if len(top_f) < k:
                top_k.append(n)
                top_f.append(freq)
                min_f = min(top_f)

            elif freq >= min_f:
                if len(top_f) >= k:
                    for i, f in enumerate(top_f):
                        if f == min_f:
                            _ = top_f.pop(i)
                            _ = top_k.pop(i)
                    
                top_k.append(n)
                top_f.append(freq)
                min_f = min(top_f)

                

        return top_k



