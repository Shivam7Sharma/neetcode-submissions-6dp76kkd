class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1= 0
        p2=0

        for i, x in enumerate(nums):
            if x==val:
                continue
            else:
                nums[p1]=nums[i]
                p1+=1
                
        return p1