# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        """
        This code defines a method delNodes that takes a binary tree (root) and a list of values to delete (to_delete). 
        The goal is to return a list of the remaining trees after deleting the specified nodes.

        The algorithm takes a binary tree (`root`) and a list of values to delete (`to_delete`). 
        It uses depth-first search (DFS) to traverse the tree and delete nodes with values in `to_delete`. 
        The remaining trees after deletion are stored in a list (`ans`). 
        
        The algorithm returns the list of remaining trees. 
        """
        to_delete = set(to_delete)
        ans = []

        def dfs(node):
            if node:
                print(f"Checking node: {node}")

                node.left = dfs(node.left)
                node.right = dfs(node.right)

                if node.val not in to_delete: 
                    return node

                print(f"Deleting node: {node}")
                if node.right: 
                    ans.append(node.right)
                if node.left: 
                    ans.append(node.left)

        start = dfs(root)

        if start:
            return ans + [start] 
        else:
            return ans
       
