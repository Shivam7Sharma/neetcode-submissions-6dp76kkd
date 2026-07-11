class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp= defaultdict(int)

        for n in nums:
            mapp[n]=mapp.get(n, 0)+1

        heap= []

        for n in mapp.keys():
            heapq.heappush(heap, [mapp[n], n])
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
                
        return res

