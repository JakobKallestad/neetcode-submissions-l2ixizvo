class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.lower().split())

        i, j = 0, len(s)-1

        while i <= j:
            print(i, j)
            while i < j and (not (ord("A") <= ord(s[i]) <= ord("z") or s[i].isdigit())):
                i += 1
            while i < j and (not (ord("A") <= ord(s[j]) <= ord("z") or s[j].isdigit())):
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

