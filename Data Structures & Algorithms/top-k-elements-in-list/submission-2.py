# from heapq import heappush,heappop
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         heap,result  = [],[]
#         for key,v in count.items():
#             heappush(heap,(v,key))
#             if len(heap)>k: heappop(heap)
#         for i in range(k):
#             result.append(heappop(heap)[1])
#         return result
class Solution:
    def topKFrequent(self,nums: List[int],k: int) -> List[int]:
        #we can use a bucket sort implementation
        count, result = Counter(nums),[]
        freq = [[] for _ in range(len(nums)+1)]
        for key,f in count.items():
            freq[f].append(key)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result)>=k:
                    return result
        return result

        