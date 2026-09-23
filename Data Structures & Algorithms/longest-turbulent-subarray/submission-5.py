class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        adjacent_sign = []
        for i, e in enumerate(arr[:-1]):
            if arr[i] == arr[i+1]:
                adjacent_sign.append(0)
            elif arr[i] < arr[i+1]:
                adjacent_sign.append(-1)
            else:
                adjacent_sign.append(1)
            
        print(adjacent_sign)

        max_res = 1
        c_res = 1
        prev = 0
        for i, e in enumerate(adjacent_sign):  # double check
            if adjacent_sign[i] == 0:
                c_res = 1
            elif adjacent_sign[i] == -prev:
                c_res += 1
            else:
                c_res = 2
            max_res = max(max_res, c_res)
            prev = adjacent_sign[i]
        return max_res