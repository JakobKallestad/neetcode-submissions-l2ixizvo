from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c_num = Counter(nums)
        limit = len(nums) // 3
        most_frequent = c_num.most_common()
        ans = []
        for a,b in most_frequent:
            if b > limit:
                ans.append(a)
        return ans