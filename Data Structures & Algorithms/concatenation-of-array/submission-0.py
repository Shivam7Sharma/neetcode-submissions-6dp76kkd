class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        l= len(nums)
        ans= [0]*2*l
        ans[0:l-1]= nums
        ans[l:]= nums
        return ans