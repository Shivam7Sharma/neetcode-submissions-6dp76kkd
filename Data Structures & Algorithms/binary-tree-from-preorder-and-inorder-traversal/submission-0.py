# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if(len(inorder)==0 or len(preorder)==0):
            return None

        node_val= preorder[0]
        start=TreeNode(node_val)
        ind= inorder.index(node_val)
        start.left=self.buildTree(preorder[1:ind+1], inorder[:ind])
        start.right=self.buildTree(preorder[ind+1:], inorder[ind+1:])

        return start