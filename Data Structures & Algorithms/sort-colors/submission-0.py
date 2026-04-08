class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket= Counter(nums)
        
        idx=0

        for x in range(3):
            for _ in range(bucket[x]):
                nums[idx]=x
                idx+=1


        


        

