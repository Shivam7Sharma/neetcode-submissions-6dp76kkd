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
        copy={}

        def dfs(node):
            if node in copy:
                return copy[node]

            nn= Node(node.val)

            copy[node]= nn
            for neigh in node.neighbors:
                nc=dfs(neigh)
                nn.neighbors.append(nc)

            return nn

        return dfs(node)
