class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        This approach is "populating next right pointers in each node" or "connecting nodes at the same level" in a binary tree.
        The code leverages recursion to traverse the tree and connects nodes based on the specified pattern.

        Here's how the code works in a nutshell:

        For each node with left and right children, connect left child to right child.
        If there is a next node, connect right child to the left child of the next node.
        Recursively apply the same process to left and right subtrees.
        This helps create a special "next" pointer relationship between nodes in the same level of the binary tree, allowing efficient traversal.
        """
        if not root:
            return None

        if root.left and root.right:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
