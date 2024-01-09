class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        implementation of a depth-first search (DFS) algorithm to clone an undirected graph.
        If the input node is None, return None (handling the base case).
        Create an empty dictionary new to keep track of the mapping between original nodes and their corresponding cloned nodes.
        Define a DFS function (dfs) that takes a node as an argument.
        Inside the DFS function:
            If the current node is already in the new dictionary, return the corresponding cloned node.
            Create a new node (copy) with the value of the current node.
            Add the mapping between the original node and its cloned copy to the new dictionary.
            Iterate through the neighbors of the original node and recursively call the DFS function on each neighbor, appending the cloned neighbors to the copy.neighbors list.
            Return the cloned copy of the current node.
        
        Finally, call the DFS function with the input node and return the cloned copy of the entire graph.
        """
        if not node:
            return None

        new ={}

        def dfs(node):
            if node in new:
                return new[node]
            
            copy = Node(node.val)
            new[node] = copy

            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        
        return dfs(node)
