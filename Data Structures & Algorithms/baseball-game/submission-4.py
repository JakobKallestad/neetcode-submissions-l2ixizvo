class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i, e in enumerate(operations):
            print(stack)
            if e == "C":
                stack.pop()
            elif e == "+":
                stack.append(stack[-1]+stack[-2])
            elif e == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(e))
        return sum(stack)
