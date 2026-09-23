class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_res = 1
        len_arr = len(arr)
        i = 0
        while i < len_arr-1:
            if arr[i] == arr[i+1]:
                i += 1
                continue
            j = i
            # case 1 - next i is bigger:
            while j < len_arr-1 and ((j % 2 == 0 and arr[j] < arr[j+1]) or (j % 2 != 0 and arr[j] > arr[j+1])):
                j += 1
            max_res = max(max_res, 1+j-i)

            # case 2 - next i is smaller:
            j = i
            while j < len_arr-1 and ((j % 2 != 0 and arr[j] < arr[j+1]) or (j % 2 == 0 and arr[j] > arr[j+1])):
                j += 1
            max_res = max(max_res, 1+j-i)
            
            i += 1
            print(i)
        return max_res