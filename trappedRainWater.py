from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        water = 0
        while r < len(height):
          while l < len(height) and height[l] == 0:
            l += 1
            r += 1
          r += 1
          loopWater = 0
          while r < len(height) and height[r] < height[l]:
            loopWater += height[l] - height[r]
            r += 1
          if r < len(height) and height[r] >= height[l]:
            water += loopWater
            l = r
          else:
            r -= 1
            maxR = r
            while (r > l):
              if height[r] > height[maxR]:
                maxR = r
                r -= 1
                continue
              water += height[maxR] - height[r]
              r -= 1
            break

        return water