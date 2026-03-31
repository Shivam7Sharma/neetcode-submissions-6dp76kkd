# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        arr=pairs

        def qs(s,e,arr):
            if e-s+1<=1:
                return arr

            pivot= e
            left=s

            for i in range(s,e):
                if arr[i].key<arr[pivot].key:
                    tmp= arr[left]
                    arr[left]=arr[i]
                    arr[i]=tmp
                    left+=1
            tmp= arr[left]
            arr[left]= arr[pivot]
            arr[pivot]= tmp

            qs(s, left-1, arr)
            qs(left+1,e,arr)

            return arr
        return qs(0,len(arr)-1,arr)

        