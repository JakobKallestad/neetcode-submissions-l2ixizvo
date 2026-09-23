class Solution:
    def decodeString(self, s: str) -> str:
        mult_stack = deque()
        char_stack = deque()
        current = []
        i = 0
        len_s = len(s)
        while i < len_s:
            c = s[i]
            if c.isdigit():
                char_stack.append(current)
                current = []
                j = i
                while c != "[":
                    j += 1
                    c = s[j]
                num = int(s[i:j])
                mult_stack.append(num)
                i = j
            elif c == "]":
                num = mult_stack.pop()
                current = char_stack.pop() + (num * current)
            else:
                current.append(c)
            i += 1
        return ''.join(current)