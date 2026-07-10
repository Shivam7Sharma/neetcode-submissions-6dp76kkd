class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        mapping= defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                i= ord(c)-ord('a')
                count[i]+=1
            mapping[tuple(count)].append(s)

        return list(mapping.values())



        