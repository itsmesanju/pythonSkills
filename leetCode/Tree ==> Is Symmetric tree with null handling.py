class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.checkNodes(root.left, root.right)
    
    def checkNodes(self,left,right):
        if left and right: #not null case
            return left.val == right.val and \
            self.checkNodes(left.left,right.right) and \
            self.checkNodes(left.right, right.left)
        return left == right

