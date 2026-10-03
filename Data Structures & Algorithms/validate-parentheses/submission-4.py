class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parenthesis_map = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            else:
                if not stack or c != parenthesis_map.get(stack.pop()):
                    return False
        return not stack
            