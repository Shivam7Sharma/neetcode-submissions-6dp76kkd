class Solution:
    def isValid(self, s: str) -> bool:

        # Lets travel once in the str
        lis=[]
        dic={"(":")","[":"]","{":"}"}

        for i, x in enumerate(s):
            print(ord(x))
            if len(lis)==0:
                lis.append(x)
                print("1st:\n")
                print(lis)
            elif lis[-1] in dic:
                if dic[lis[-1]]==x:
                    lis.pop()
                    print("2nd: \n")
                    print(lis)

                else:
                    lis.append(x)
                    print("3rd: \n")
                    print(lis)


        return True if len(lis)==0 else False

        