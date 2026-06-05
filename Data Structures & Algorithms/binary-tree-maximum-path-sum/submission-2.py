# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode],memo={}) -> int:
        result = [root.val]
        def dfs(node):
            if not node: return 0
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            #ignore the negatives
            leftPath,rightPath = max(leftPath,0), max(rightPath,0)
            #if we considering the path left -> root -> right
            result[0] = max(result[0],leftPath+rightPath+node.val)
            return max(leftPath,rightPath) + node.val
        dfs(root)
        return result[0]
        