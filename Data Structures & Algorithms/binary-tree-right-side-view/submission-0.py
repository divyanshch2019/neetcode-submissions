# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        q = deque([root])
       
        while q:
            size = len(q)
            first_node = True
            for _ in range(size):
                current = q.popleft()
                if first_node:
                    result.append(current.val)
                    first_node =  False
                if current.right: q.append(current.right)
                if current.left: q.append(current.left)
        return result

        