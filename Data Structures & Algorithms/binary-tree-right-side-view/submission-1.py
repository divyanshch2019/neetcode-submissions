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
            for i in range(size):
                current = q.popleft()
                if size-1 ==i:
                    result.append(current.val)
                if current.left: q.append(current.left)
                if current.right: q.append(current.right)
                
        return result

        