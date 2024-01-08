# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """
        This code is an implementation of finding the diameter of a binary tree using a recursive approach. The diameter of a binary tree is defined as the length of the longest path between any two nodes in a tree. The path may or may not pass through the root.
        """
        maxd = 0  # Variable to store the maximum diameter

        def longest_path(root):
            if root is None:
                return 0

            left = longest_path(root.left)   # Length of the longest path in the left subtree
            right = longest_path(root.right)  # Length of the longest path in the right subtree

            nonlocal maxd
            # Update the maximum diameter if the sum of left and right paths is greater. We are adding this because it will form the diameter.
            maxd = max(maxd, left + right)

            # Return the length of the longest path starting from the current node
            return 1 + max(left, right)

        # Start the recursion from the root of the binary tree
        longest_path(root)

        # Return the maximum diameter found during the traversal
        return maxd
