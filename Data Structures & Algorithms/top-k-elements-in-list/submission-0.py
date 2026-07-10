class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp= defaultdict(int)
                
        for n in nums:
            if n not in mapp:
                mapp[n]=1
            else:
                mapp[n]+=1

        nums=sorted(nums, key= lambda element: mapp[element], reverse=True)
        ans=[]
        for n in nums:
            if n not in ans and k>0:
                ans.append(n)
                k-=1

        return ans
