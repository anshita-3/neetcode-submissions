# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        q=deque([root])
        res=[]
        while q:
            rightnode=None
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node:
                    rightnode=node
                    q.append(node.left)
                    q.append(node.right)
            if rightnode:
                res.append(rightnode.val)
        return res