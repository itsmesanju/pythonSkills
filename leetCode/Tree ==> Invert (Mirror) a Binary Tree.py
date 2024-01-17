class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None

    # Swap left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# Example usage:
# Construct a sample binary search tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the binary search tree
inverted_root = invert_tree(root)

# Print the inverted tree (in-order traversal)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
       
