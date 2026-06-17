# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        if not root: return level_order
        q = deque([root])
        while q:
            temp_level = []
            size = len(q)
            for _ in range(size):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                temp_level.append(current.val)
            level_order.append(temp_level)
        return level_order
        