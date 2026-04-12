from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def binary_search(low, high):
            ans=high
            while low<=high:
                mid =(low+high)//2
                if ismin(mid)==-1:
                    low=mid+1
                else:
                    ans=mid
                    high= mid-1

            return ans


        def ismin(mid):

            total=sum(ceil(pile/mid) for pile in piles)
            if total<=h :
                return 1
            elif total>h :
                return -1

            return mini

        return binary_search(1,max(piles))