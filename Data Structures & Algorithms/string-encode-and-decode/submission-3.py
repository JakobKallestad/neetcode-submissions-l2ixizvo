class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(str(len(word)))
            output.append("#")
            output.append(word)
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        output = []
        temp_word = []
        remaining_add = 0
        i = 0
        while i < len(s):
            if remaining_add == 0:
                if i != 0:
                    if temp_word:
                        output.append(''.join(temp_word))
                        temp_word = []
                    else:
                        output.append("")
                next_remaining_add = []
                while s[i].isdigit():
                    next_remaining_add.append(s[i])
                    i += 1
                print(next_remaining_add)
                remaining_add = int(''.join(next_remaining_add))
            else:
                temp_word.append(s[i])
                remaining_add -= 1
            i += 1
        if temp_word:
            output.append(''.join(temp_word))
        else:
            output.append("")
        return output
                

                