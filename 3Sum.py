from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            twoSum = self.twoSum(nums, -num, i + 1)
            if len(twoSum) != 0:
                for l in twoSum:
                    l.append(num)
                    res.append(l)
      
        return res

    def twoSum(self, nums: List[int], target: int, begin: int) -> List[List[int]]:
        res = []
        beg = begin
        end = len(nums) - 1

        while beg < end:
            if beg > begin and end < len(nums) - 1:
                if nums[beg - 1] == nums[beg] and nums[end + 1] == nums[end]:
                    beg += 1
                    end -= 1
                    continue

            val = nums[beg] + nums[end] 
            if val < target:
                beg += 1
            elif val > target:
                end -= 1
            else:
                res.append([nums[beg], nums[end]])
                beg += 1
                end -= 1

        return res