from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        pair_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c in pair_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                c2 = stack.pop()
                if pair_map[c2] != c:
                    return False
        if not stack:
            return True
        else:
            return False
        