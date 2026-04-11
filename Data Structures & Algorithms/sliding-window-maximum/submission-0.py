from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        solution = []
        bst = SortedList()
        nums = nums
        len_nums = len(nums)
        # prep-work
        for i in range(k):
            bst.add(nums[i])

        for i in range(len_nums-k+1):
            solution.append(bst[-1])
            to_remove = nums[i]
            bst.remove(to_remove)
            if i+k < len_nums:
                to_add = nums[i+k]
                bst.add(to_add)

        return solution



        