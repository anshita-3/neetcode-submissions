# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftheight=self.heightMax(root.left)
        rightheight=self.heightMax(root.right)
        diameter=leftheight+rightheight
        sub=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

        return max(diameter,sub)

    def heightMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.heightMax(root.left),self.heightMax(root.right))
