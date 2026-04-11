from collections import defaultdict

class Solution:
    def trap(self, height: List[int]) -> int:

        layer_area = defaultdict(int)
        for h in height:
            for a in range(h):
                layer_area[a] += 1
        print(layer_area)

        i, j = 0, len(height)-1
        water_area = 0
        sea_level = 0
        while i < j:
            diff_length = j - i - 1
            i_peak = height[i]
            j_peak = height[j]
            min_peak = min(i_peak, j_peak)
            #diff_height = min_peak - sea_level
            #if diff_height > 0:
            for k in range(sea_level, min_peak):
                # ignore solid layer area inbetween peaks:
                solid_inbetween = layer_area[k] - 2
                to_add = diff_length - solid_inbetween
                print(to_add)
                print()
                water_area += to_add
                sea_level += 1 #min_peak
            if i_peak < j_peak:
                i += 1
                for k in range(i_peak):
                    layer_area[k] -= 1
            else:
                j -= 1
                for k in range(j_peak):
                    layer_area[k] -= 1
        return water_area
            
            
            

