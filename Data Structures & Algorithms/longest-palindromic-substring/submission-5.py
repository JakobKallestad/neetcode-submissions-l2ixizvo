class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        
        # odd
        for i in range(len(s)):
            j, k = i, i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k-j+1 > res_len:
                    res_len = k-j+1
                    res = s[j:k+1]
                j -= 1
                k += 1
        
        # even
        for i in range(len(s)):
            j, k = i, i+1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k-j+1 > res_len:
                    res_len = k-j+1
                    res = s[j:k+1]
                j -= 1
                k += 1

        return res