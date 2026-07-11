class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp= defaultdict(int)

        for n in nums:
            mapp[n]=mapp.get(n, 0)+1

        nums=sorted(nums,key= lambda element:mapp[element], reverse=True)
        res=[]
        
        for n in nums:
            if n not in res and k>0:
                res.append(n)
                k-=1

        return res

