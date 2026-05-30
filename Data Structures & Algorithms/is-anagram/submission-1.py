class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ad={}
        bd={}
        if(len(s)!=len(t)):
            return False
        
        
        for x in s:
            if x in ad:
                ad[x]+=1
            else:
                ad[x]=1

        for y in t:
            if y in bd:
                bd[y]+=1
            else:
                bd[y]=1

        for k in ad.keys():
            if k in bd.keys() and bd[k]==ad[k]:
                continue
            else:
                return False

        return True