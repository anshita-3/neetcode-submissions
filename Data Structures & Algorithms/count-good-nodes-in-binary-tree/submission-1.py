# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count=0
        from collections import deque
        q=deque()
        q.append((root,-float('inf')))
        while q:
            node,maxval=q.popleft()
            if node.val>=maxval:
                count+=1
            newmax=max(maxval,node.val)
            if node.left:
                q.append((node.left,newmax))
            if node.right:
                q.append((node.right,newmax))
        return count 



