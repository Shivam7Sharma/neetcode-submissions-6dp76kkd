class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #in-place
        lis=nums
        ans=0
        for i,x in enumerate(lis):
            print(i)
            if x not in nums[:i]:
                print("the curr is:",nums[i])
                print("the value to write is: ", x)
                nums[ans]=x
                ans+=1
            else:
                continue
        print(nums)
        return ans
        