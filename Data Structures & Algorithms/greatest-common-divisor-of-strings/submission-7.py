from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 2 cases:
        if str1 in str2:
            b = str2
            a = str1
        elif str2 in str1:
            a = str2
            b = str1
        else:
            return ""

        len_a = len(a)
        len_b = len(b)

        gcd_ab = gcd(len_a, len_b)
        print(gcd_ab)

        for i in range(0, len_b, gcd_ab):
            if b[i:i+gcd_ab] != a[:gcd_ab]:
                break
        else:
            return a[:gcd_ab]
        
        return ""
