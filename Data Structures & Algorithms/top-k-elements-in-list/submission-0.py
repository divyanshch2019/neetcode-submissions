class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count,freq = {}, [[] for i in range(len(nums)+1)]
        result = []
        for n in nums:
            count[n] = 1+count.get(n,0)
        for num,f in count.items():
            freq[f].append(num)

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) ==k:
                    #condition met,return result
                    return result

        
        