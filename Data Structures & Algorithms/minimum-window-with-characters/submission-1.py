from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0, 0
        len_t = len(t)
        sol = s+s
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        
        current = defaultdict(int)
        n_matches = 0
        while j < len(s):
            c = s[j]
            if current[c] < target[c]:  # means that c is a MATCH and more of c is needed
                n_matches += 1
            current[c] += 1  # otherwise its still counted, but not an immediate needed MATCH

            while n_matches == len_t:
                if (j-i+1) < len(sol):
                    sol = s[i:j+1]
                c2 = s[i]
                current[c2] -= 1
                if current[c2] < target[c2]:
                    n_matches -= 1
                i += 1

            j += 1

        return "" if sol == s+s else sol