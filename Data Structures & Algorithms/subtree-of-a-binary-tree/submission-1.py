# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self,root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)

        return False


    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        elif root is None:
            return False
        elif self.dfs(root,subRoot):
            return True

        l=self.isSubtree(root.left, subRoot)
        r=self.isSubtree(root.right, subRoot)

        return l or r
                                
