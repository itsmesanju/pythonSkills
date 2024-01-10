# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Find the height of the left and right subtree with inner dfs function. 
        If at any point the height differs by one then we make the balanced boolean false.
        """
        balanced = True
        
        def dfs(root):
            nonlocal balanced
            
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) > 1:
               balanced = False
          
            return 1 + max(left,right)
  
        dfs(root)
        return balanced
