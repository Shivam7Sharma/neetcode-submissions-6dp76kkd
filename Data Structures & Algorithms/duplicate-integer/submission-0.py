class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash={}

        for x in nums:
            if x in hash:
                hash[x]+=1
                return True
            else:
                hash[x]=1
                
        return False
        