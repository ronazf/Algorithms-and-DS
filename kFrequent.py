class Solution:
    def kFrequent(nums: list[int], k: int) -> list[int]:
        hashmap = {}
        heap = [[] for _ in range(len(nums))]
        res = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key in hashmap:
            heap[hashmap[key] - 1].append(key)
        
        for i in range(len(nums)):
            if heap[-(i + 1)] != []:
                res += heap[-(i + 1)]
            if len(res) == k:
                break;
        
        return res
        
        
        
        