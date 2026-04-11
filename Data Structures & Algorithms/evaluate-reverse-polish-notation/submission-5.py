from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        for t in tokens:
            print(t, end=" ")
        print()
        stack = deque()
        for t in tokens:
            if not t.lstrip('-').isdigit():
                print(stack)
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    c = a + b
                elif t == "-":
                    c = a - b
                elif t == "*":
                    c = a * b
                elif t == "/":
                    c = int(a / b)
                stack.append(c)
            else:
                stack.append(int(t))
        return stack[0]
