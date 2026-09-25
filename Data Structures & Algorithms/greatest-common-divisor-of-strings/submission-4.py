class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 2 cases:
        if str1 in str2:
            long_str = str2
            short_str = str1
        elif str2 in str1:
            short_str = str2
            long_str = str1
        else:
            return ""

        for i in range(len(short_str)):
            if i == 0:
                candidate_str = short_str
            else:
                candidate_str = short_str[:-i]
            if  len(long_str) % len(candidate_str) == 0:
                for j in range(0, len(short_str), len(candidate_str)):
                    if candidate_str != short_str[j:j+len(candidate_str)]:
                        break
                else:
                    for j in range(0, len(long_str), len(candidate_str)):
                        if candidate_str != long_str[j:j+len(candidate_str)]:
                            break
                    else:
                        return candidate_str  # maybe --> need to confirm
        return ""