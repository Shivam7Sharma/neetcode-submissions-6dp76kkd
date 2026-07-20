class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()

        for i, a in enumerate(nums):

            if a>0: 
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            
            l= i+1
            r= len(nums)-1
            

            while l<r:
                threeSum= nums[i]+ nums[l]+ nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l-1]==nums[l]:
                            l+=1

        return res