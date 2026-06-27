# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        queue = deque([root])
        leftToRight = True

        while queue:

            size = len(queue)
            level = [0] * size

            for i in range(size):

                node = queue.popleft()

                if leftToRight:
                    index = i
                else:
                    index = size - 1 - i

                level[index] = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(level)
            leftToRight = not leftToRight

        return ans
        