class Solution:
    def compress(self, chars: List[str]) -> int:
        len_chars = len(chars)
        count = 1
        res = []
        index = 0
        for i, c in enumerate(chars):
            nxt = chars[i+1] if i+1 < len_chars else None
            if c == nxt:
                count += 1
            else:
                chars[index] = c
                index += 1
                if count > 1:
                    for c2 in list(str(count)):
                        chars[index] = c2
                        index += 1
                count = 1
        return index
