class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-stone for stone in stones]
        heapq.heapify(stones)

        while(len(stones)>=2):
            y= heapq.heappop(stones)
            x= heapq.heappop(stones)
            x=-1*x
            y=-1*y
            if x==y:
                continue
            
            elif y>x:
                heapq.heappush(stones, -1*(y-x))

        
        if len(stones)==1:
            return -1*heapq.heappop(stones)

        return 0;
        