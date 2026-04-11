from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([0])
        solution = {}
        for j, t in enumerate(temperatures[1:], start=1):
            while stack and temperatures[stack[-1]] < t:
                i = stack[-1]
                solution[i] = j-i
                stack.pop()
            stack.append(j)
        
        while stack:
            i = stack.pop()
            solution[i] = 0
        
        solution = [solution[k] for k in sorted(solution)]
        return solution

