from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0

        minVal = prices[0]
        maxVal = 0
        diff = 0

        for price in prices:
            minVal = min(minVal, price)
            maxVal = price
            diff = max(maxVal - minVal, diff)
        
        return diff