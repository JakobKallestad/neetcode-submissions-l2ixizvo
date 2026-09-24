class Solution:
    def jump(self, nums: List[int]) -> int:

        queue = deque()
        queue.appendleft((0, 0)) # (c_ind, c_steps)
        visited = defaultdict(int)
        visited[0] = 0
        
        while queue:
            c_ind, c_steps = queue.pop()
            c_val = nums[c_ind]
            neighbors = min(c_val, len(nums)-c_ind-1)+1 # todo

            for j in range(c_ind, c_ind+neighbors):
                if j not in visited:
                    visited[j] = c_steps+1
                    queue.appendleft((j, c_steps+1))
        return visited[len(nums)-1]



