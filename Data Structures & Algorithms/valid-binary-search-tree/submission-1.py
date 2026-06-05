# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BSTUtil(node,min_val,max_val):
            if not node:
                return True
            if node.val not in range(min_val,max_val+1):
                return False
            return BSTUtil(node.left,min_val,node.val-1) and BSTUtil(node.right, node.val+1,max_val) 
        return BSTUtil(root,-100000,100000)