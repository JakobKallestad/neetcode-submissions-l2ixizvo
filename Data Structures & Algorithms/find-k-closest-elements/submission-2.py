class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # observations:
        # target O(log(n)+k) --> then its still kinda linear...
        # binary search to find the approximate point of x
        # then do k iterations of comparisons between 2 numbers
        # whatever, i'll just ignore binary search for now.
        output = deque()

        j = 0
        while j < len(arr) and arr[j] < x:
            j += 1
        i = j-1

        if j == len(arr):
            return arr[::-1][:k][::-1]

        for _ in range(k):
            if j == len(arr) or (abs(arr[i] - x) < abs(arr[j] - x) or (abs(arr[i] - x) == abs(arr[j] - x) and arr[i] < arr[j])):
                output.appendleft(arr[i])
                i -= 1
            else:
                output.append(arr[j])
                j += 1
        
        return list(output)