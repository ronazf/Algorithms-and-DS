from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        q = collections.deque()
        res = []
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            if l > q[0]:
                q.popleft()
        
        return res