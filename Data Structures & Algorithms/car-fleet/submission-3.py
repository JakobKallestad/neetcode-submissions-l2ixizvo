from collections import deque
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars = sorted(cars, key=lambda x: x[0])
        n_cars = len(cars)
        n_fleets = 1
        i = n_cars-1
        while i > 0:
            c_pos, c_speed = cars[i]
            i -= 1
            while i >= 0:
                n_pos, n_speed = cars[i]
                if n_speed <= c_speed:
                    n_fleets += 1
                    break
                else:
                    c_remaining_time = (target - c_pos) / c_speed
                    n_remaining_time = (target - n_pos) / n_speed
                    if c_remaining_time < n_remaining_time:
                        n_fleets += 1
                        break
                i -= 1
        return n_fleets

            
