class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hpq = []
        heapq.heapify(hpq)
        for p in points:
            dist = (p[0] ** 2) + (p[1] ** 2)
            heapq.heappush(hpq, (dist, p))
        ans = []
        for i in range(k):
            dist,p1=heapq.heappop(hpq)
            ans.append(p1)

        return ans
