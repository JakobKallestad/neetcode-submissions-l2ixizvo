class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, a in enumerate(numbers):
            for j, b in enumerate(numbers):
                if j <= i:
                    continue
                if a + b == target:
                    return [i+1, j+1]
        
        