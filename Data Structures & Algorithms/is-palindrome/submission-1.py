class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st=''

        for c in s:
            if c.isalnum():
                st=st+c.lower()

        return st[::-1]==st
