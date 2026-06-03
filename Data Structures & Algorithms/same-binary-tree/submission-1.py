# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def recur(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val==q.val:
                l=recur(p.left, q.left)
                r=recur(p.right, q.right)
                return l and r
            else:
                return False

        return recur(p,q)