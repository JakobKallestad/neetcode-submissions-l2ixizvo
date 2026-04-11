class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        # odd
        for i in range(len(s)):
            j, k = i, i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                res += 1
                j -= 1
                k += 1
        
        # even
        for i in range(len(s)):
            j, k = i, i+1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                res += 1
                j -= 1
                k += 1

        return res