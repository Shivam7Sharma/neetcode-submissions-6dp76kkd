"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        oldtonew={}
        q= deque()
        nn=Node(node.val)
        oldtonew[node]= nn
        q.append(node)
        

        while q:
            n=q.popleft()

            for neigh in n.neighbors:
                if neigh not in oldtonew:
                    newn=Node(neigh.val)
                    oldtonew[neigh]=newn
                    q.append(neigh)

                oldtonew[n].neighbors.append(oldtonew[neigh])

        return oldtonew[node]



