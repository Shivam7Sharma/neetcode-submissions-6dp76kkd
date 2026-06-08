# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def recur(root,p,q):
            if root==None or root.val==q.val or root.val==p.val:
                return root

            left= recur(root.left, p,q)
            right= recur(root.right, p,q)
            if left and right:
                return root      # p on one side, q on other
            elif left:
                return left      # both on left subtree
            else:
                return right     # both on right subtree


        lca=recur(root,p,q)
        return lca