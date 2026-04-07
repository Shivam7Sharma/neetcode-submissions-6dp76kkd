# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def qs(pairs, s,e):
            if e-s+1<=1:
                return pairs

            left=s
            pivot= e

            for i in range(s,e):
                if pairs[i].key<pairs[pivot].key:
                    tmp= pairs[i]
                    pairs[i]= pairs[left]
                    pairs[left]= tmp
                    left+=1

            tmp=pairs[pivot]
            pairs[pivot]= pairs[left]
            pairs[left]= tmp

            qs(pairs,s,left-1)
            qs(pairs,left+1,e)

            return pairs

        return qs(pairs, 0, len(pairs)-1)