class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r= len(height)-1

        res=0
        leftmax, rightmax= height[l], height[r]
        while l<r:
            if height[l]<height[r]:
                l+=1
                leftmax= max(height[l], leftmax)
                res+=leftmax-height[l]

            else:
                r-=1
                rightmax= max(height[r], rightmax)
                res+=rightmax- height[r]

        return res