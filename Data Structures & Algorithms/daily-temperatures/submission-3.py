from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([0])
        solution = [0]*len(temperatures)
        for j, t in enumerate(temperatures[1:], start=1):
            while stack and temperatures[stack[-1]] < t:
                i = stack[-1]
                solution[i] = j-i
                stack.pop()
            stack.append(j)
        return solution

