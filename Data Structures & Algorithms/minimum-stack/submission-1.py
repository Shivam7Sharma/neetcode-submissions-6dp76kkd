class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini)>0:
            if self.mini[-1]>=val:
                self.mini.append(val)
            else:
                self.mini.append(self.mini[-1])
        elif len(self.mini)==0:
            self.mini.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mini)>0:
            return self.mini[-1]

            
        


