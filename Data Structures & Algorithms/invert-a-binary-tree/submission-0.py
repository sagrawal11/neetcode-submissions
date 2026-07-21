# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # to invert the tree, you need to turn all the left nodes right and all the right nodes left

        if root is None:
            return

        root.left, root.right = root.right, root.left # swap the left and right
        self.invertTree(root.left) # go down the left subtree and swap everything
        self.invertTree(root.right) # go down the right subtree and swap everything

        return root