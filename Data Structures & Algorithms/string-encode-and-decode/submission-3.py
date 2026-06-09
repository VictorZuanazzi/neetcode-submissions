class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for text in strs:
            sizes.append(f"{len(text):03}")

        enconded = ";".join(sizes) + "/" + "".join(strs)

        return enconded

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return []

        sizes_str = s.split("/")[0]
        start = len(sizes_str) + 1

        sizes = [int(_s) for _s in sizes_str.split(";")]
        strs = []
        for size in sizes:
            end = start + size
            strs.append(s[start:end])
            start = end

        return strs