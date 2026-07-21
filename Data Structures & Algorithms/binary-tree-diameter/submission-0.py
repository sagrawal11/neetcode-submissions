# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we want to find the length of this binary tree, which is just the max paths between any two nodes in the binary tree
        # this is just num nodes - 1 from the two most distance nodes
        # one thing to note, the length will always pass through a root of some kind

        self.length = 0

        def helper(node):
            if node is None:
                return 0
            
            self.current_length = 0
            left = helper(node.left)
            right = helper(node.right)

            if left + right > self.length:
                self.length = left + right

            return 1 + max(left, right)
            
        helper(root)
        return self.length




        
        