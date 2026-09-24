class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # observations
        # A) positive numbers at the right-end --> add to final result and remove
        # B) negative numbers at the left-end --> add to final results and remove
        # C) find "latest" postiive number at left-side. start colisions.

        result = []
        stack = deque()
        for i, a in enumerate(asteroids):
            if a < 0:
                if stack:
                    while stack: # collide until finished
                        left = stack.pop()
                        right = a
                        if left > abs(right):
                            stack.append(left)
                            break # crush right
                        elif left < abs(right):
                            continue
                        else:
                            break
                    else:
                        # we didnt break out (right is alive)
                        result.append(right)
                else:
                    result.append(a)
            else:
                stack.append(a)
        
        # empty stack:
        while stack:
            result.append(stack.popleft())
        
        return result

