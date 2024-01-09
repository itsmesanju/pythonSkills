# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        Make a recursive call on the node and the level of the node starting with 0. 
        Then just add level and node.val to the dictionary or append it and return the resuls
        """
        def dfs(root, level):
            print(root, level)
            if root is None:
                return

            result[level] = result.get(level, []) + [root.val]

            dfs(root.left, level+1)
            dfs(root.right, level+1)


        result = {}
        dfs(root, 0)
        return result.values()


#BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
         This code uses a breadth-first search (BFS) approach with a queue.

        Initialize an empty list res to store the final result.
        Create a deque (q) and enqueue the root node into it.
        Perform BFS using the deque. At each level, dequeue the nodes, add their values to the current level list, and enqueue their left and right children.
        Append the level list to the result (res) if it is not empty.
        Repeat the process until the deque is empty.

        """
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level=[]

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        return res

