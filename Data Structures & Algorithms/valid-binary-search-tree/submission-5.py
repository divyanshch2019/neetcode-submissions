# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev,current,q = float('-inf'), root,[]
        while current or q:
            while current:
                q.append(current)
                current = current.left
            #if you are here, then we traversed all the left nodes
            current = q.pop()
            if current.val <= prev:
                return False
            prev = current.val
            current = current.right
        return True
        