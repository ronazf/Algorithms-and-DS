from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        product = 1
        for i, num in enumerate(nums):
            if i != length - 1:
                product *= num
                res[i + 1] = product
      
        product = 1
        for i in range(length - 1, 0, -1):
            product *= nums[i]
            res[i - 1] = product * res[i - 1]
      
        return res