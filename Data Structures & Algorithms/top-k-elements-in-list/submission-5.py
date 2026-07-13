class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        frequency=[[]for i in range(len(nums)+1)]

        for n in nums:
            count[n]= count.get(n,0)+1
        
        for num, f in count.items():
            frequency[f].append(num)
        res=[]
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res)==k:
                    return res


