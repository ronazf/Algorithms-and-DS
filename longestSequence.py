from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in hashmap:
                counter = 0
                while num + counter in hashmap:
                    counter += 1
                longest = max(longest, counter)
        
        return longest