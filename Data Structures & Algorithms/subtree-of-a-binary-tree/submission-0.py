# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        # let's first write a helper function to determine if two subtrees are exactly identical
        def identical(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root.val != subRoot.val:
                return False
            return identical(root.left, subRoot.left) and identical(root.right, subRoot.right)
        
        # now we need to recursively check if root or it's left and right branches are identical to the subroot

        if identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        