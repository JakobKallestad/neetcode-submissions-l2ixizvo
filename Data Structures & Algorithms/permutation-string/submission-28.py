from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = defaultdict(int)
        for c in s1:
            target[c] += 1
        
        i, j = 0, 0
        current = defaultdict(int)
        while j < len(s2):
            print(i, j, current)
            c = s2[j]
            if c not in target: # reset in front
                j += 1
                i = j
                current = defaultdict(int)
                continue
            current[c] += 1
            while current[c] > target[c]:  # ran into a problem. must shorten lefthand side
                current[s2[i]] -= 1 
                i += 1
                j = max(j, i)

            print("P2", i, j, current)
            print()
            # if we find all the characters in the substring we can return True
            if (j-i)+1 == len(s1):
                return True
            j += 1
        return False
