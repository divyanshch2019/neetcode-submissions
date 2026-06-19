# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return 
        if p.val < q.val and root.val in range(p.val,q.val+1) or p.val > q.val and root.val in range(q.val,p.val+1):
            #the current root is the LCA
            return root
        if p.val <=root.val and q.val<=root.val:
            #go left
            return self.lowestCommonAncestor(root.left, p,q)
        elif p.val >=root.val and q.val>=root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        