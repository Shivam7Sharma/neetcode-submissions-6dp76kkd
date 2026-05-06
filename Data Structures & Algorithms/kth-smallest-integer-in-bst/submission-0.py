# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #global ans
        ans=[]
        self.count = 0

        def inorder(root, ans):
            if root is None:
                return

            inorder(root.left, ans)
            self.count += 1
            if self.count == k:
                ans.append(root.val)
                return

            inorder(root.right, ans)

            return

        inorder(root, ans)
        return ans[0]
