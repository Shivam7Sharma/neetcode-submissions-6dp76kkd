# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(pairs,x1,m,x2):
            L= pairs[x1:m+1]
            R= pairs[m+1:x2+1]

            i=0
            j=0
            k=x1

            while i< len(L) and j<len(R):
                if R[j].key<L[i].key:
                    pairs[k]=R[j]
                    j+=1
                else:
                    pairs[k]= L[i]
                    i+=1
                k+=1

            while i<len(L):
                pairs[k]=L[i]
                i+=1
                k+=1

            while j<len(R):
                pairs[k]= R[j]
                j+=1
                k+=1

        def merge_sort(pairs, x1, x2):
            if x2-x1<=0:
                return pairs
            m=x1+ (x2-x1)//2
            merge_sort(pairs,x1,m)
            merge_sort(pairs,m+1,x2)

            merge(pairs, x1,m,x2)

        merge_sort(pairs, 0, len(pairs)-1)
        return pairs

