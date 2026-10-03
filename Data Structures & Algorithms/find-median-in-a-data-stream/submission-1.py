class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        
        l, r = 0, len(self.nums)-1
        while l <= r:
            m = (l+r) // 2
            if self.nums[m] < num:
                l = m+1
            else:
                r = m-1
        self.nums.insert(l, num)

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            a, b = len(self.nums)//2-1, len(self.nums)//2
            return (self.nums[a] + self.nums[b])/2
        else:
            return self.nums[len(self.nums)//2]
        