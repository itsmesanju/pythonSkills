"""
Serialization (serialize method):
==================================
Utilizes a recursive depth-first search (DFS) approach.
Converts the binary tree into a string by traversing it in pre-order.
Nodes are represented by their values, and null nodes are denoted by '#'.
Returns the serialized string.

Deserialization (deserialize method):
=====================================
Splits the input string by commas to get a list of values.
Utilizes a recursive DFS approach to reconstruct the binary tree from the list.
Handles '#' as null nodes.
Returns the root of the deserialized binary tree.
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        def dfs(root):
            if not root:
                s.append('#')
                return
            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(s)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def dfs(data):
            node = data.pop(0)
            if node == '#':
                return
            tree = TreeNode(node)
            tree.left = dfs(data)
            tree.right = dfs(data)
            return tree
        
        return dfs(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
