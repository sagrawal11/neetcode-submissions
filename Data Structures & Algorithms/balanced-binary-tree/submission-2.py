# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if node is None:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if left == -1 or right == -1: # this is needed in case one of the subtrees is already unbalanced
                return -1

            if abs(left - right) > 1: # 1 is acceptable, anything greater isn't
                return -1
            return 1 + max(left, right)

        if helper(root) == -1:
            return False
        return True
            