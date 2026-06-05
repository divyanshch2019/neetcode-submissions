from heapq import heappush,heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap,result  = [],[]
        for key,v in count.items():
            heappush(heap,(v,key))
            if len(heap)>k: heappop(heap)
        for i in range(k):
            result.append(heappop(heap)[1])
        return result

        