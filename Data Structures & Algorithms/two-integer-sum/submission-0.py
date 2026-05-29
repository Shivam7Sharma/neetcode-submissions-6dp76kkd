class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,x in enumerate(nums):
            need= target-x
            if need in hash.keys():
                return [hash[need],i ]
            else:
                hash[x]=i

        return []