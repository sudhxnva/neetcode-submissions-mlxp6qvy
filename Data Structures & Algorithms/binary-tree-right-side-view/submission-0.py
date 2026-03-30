# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()

        res = []

        if root:
            q.append(root)
            res.append(root.val)

        while q:
            seen = False
            for _ in range(len(q)):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                    if not seen:
                        res.append(node.right.val)
                        seen = True
                if node.left:
                    q.append(node.left)
                    if not seen:
                        res.append(node.left.val)
                        seen = True

        return res