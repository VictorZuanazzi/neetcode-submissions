class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def _is_anagram(w1, w2):
            if len(w1) != len(w2):
                return False

            def _build_map(w):
                map = {}
                for c in w:
                    map[c] = 1 + map.get(c, 0)
                return map

            map1 = _build_map(w1)
            map2 = _build_map(w2)

            for c, freq in map1.items():
                if freq != map2.get(c, 0):
                    return False
            return True

        lengh_map = {}
        for word in strs:
            l = len(word)
            if l not in lengh_map.keys():
                lengh_map[l] = [[word]]

            else:
                inserted = False
                for i, w_list in enumerate(lengh_map[l]):
                    if _is_anagram(w_list[0], word):
                        w_list.append(word)
                        inserted = True
                        continue
                if not inserted:
                    lengh_map[l].append([word])

        final_output = []
        for v in lengh_map.values():
            final_output.extend(v)

        return final_output
