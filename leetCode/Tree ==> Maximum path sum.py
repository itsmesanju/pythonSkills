class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_path_sum(root):
    def max_gain(node):
        nonlocal max_sum

        if node is None:
            return 0

        # Calculate the maximum gain for the left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Update the maximum path sum considering the current node
        current_path_sum = node.value + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)

        # Return the maximum gain for the subtree rooted at the current node
        return node.value + max(left_gain, right_gain)

    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    max_gain(root)  # Start the recursive calculation

    return max_sum

# Example usage:
# Construct a sample binary tree
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

result = max_path_sum(root)
print("Maximum Path Sum:", result)
