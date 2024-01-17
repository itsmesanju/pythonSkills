class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True

    return False
