from collections import defaultdict, deque

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.store[key]
        l, r = 0, len(candidates)-1
        c_best = ""
        while l <= r:
            mid = (l + r) // 2
            val, prev_t = candidates[mid]
            if prev_t < timestamp:
                l = mid + 1
                c_best = val
            elif prev_t > timestamp:
                r = mid -1
            else:
                return val
        return c_best
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)