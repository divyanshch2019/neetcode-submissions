# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if min(p.val,q.val)<=cur.val<=max(q.val,p.val):
                #the current root is the LCA
                return cur
            if p.val <=cur.val and q.val<=cur.val:
                #go left
                cur = cur.left
            elif p.val >=cur.val and q.val>=cur.val:
                cur = cur.right
        