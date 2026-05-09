# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        level = 0
        if root is None:
            return []
        queue.append(root)
        ans = [[root.val]]
        while len(queue) > 0:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    tmp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    tmp.append(node.right.val)
            if len(tmp)>0:
                ans.append(tmp)
                level += 1

        return ans
