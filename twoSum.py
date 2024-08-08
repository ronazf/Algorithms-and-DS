class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in hashmap:
                return [hashmap[compl], i]
        
            hashmap[nums[i]] = i