# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        def dfs(root):
            if root is None:
                return 0
            lcount=dfs(root.left)
            if lcount==-1:
                return -1
            rcount=dfs(root.right)
            if rcount==-1:
                return -1

            if abs(lcount-rcount)>1:
                return -1
            return 1+ max( lcount, rcount)



        return dfs(root)!=-1