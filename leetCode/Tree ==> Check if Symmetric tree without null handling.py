def subFunction(lf, rt):
    if not lf or not rt:
        return True
    return (lf and rt) and subFunction(lf.left, rt.right) and subFunction(lf.right, rt.left)

def isSymmetric(self, root: TreeNode) -> bool:
     return subFunction(root.left, root.right)
 
#### Class format.

class Solution:
    def subFunction(self,lf, rt):
        if not lf or not rt:
            return True
        return (lf and rt) and self.subFunction(lf.left, rt.right) and self.subFunction(lf.right, rt.left)

    def isSymmetric(self, root: TreeNode) -> bool:
         return self.subFunction(root.left, root.right)
#Failed test...
#[1,2,2,null,3,null,3]
