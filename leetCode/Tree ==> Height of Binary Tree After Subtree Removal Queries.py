"""
Store the answers for every node. The answer for any node would be the depth till now plus the height of the complementary tree (right tree if node is left, and vice versa)
"""
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        @cache
        def height(node):
            return 0 if not node else 1 + max(height(node.left), height(node.right))
        
        answer = {}
        
        def dfs(node, depth, remaining_tree_height_after_current_node_removal):
            if not node: return
            answer[node.val] = remaining_tree_height_after_current_node_removal
            dfs(node.left, depth + 1, max(remaining_tree_height_after_current_node_removal, depth + height(node.right)))
            dfs(node.right, depth + 1, max(remaining_tree_height_after_current_node_removal, depth + height(node.left)))

        dfs(root, 0, 0)
        return map(answer.get, queries)
