from collections import Counter
import heapq
class Solution:
    #TC = O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        result = []
        for num,freq in freq_map.items():
            buckets[freq].append(num)
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result