from collections import defaultdict, deque

"""
The given code is an implementation of a solution to determine whether a given undirected graph is a valid tree. 
The code uses breadth-first search (BFS) to traverse the graph and checks for the presence of cycles.

Mark the first node as visited.
Use a deque to perform BFS.
Traverse the graph using BFS.
Remove edges during traversal to prevent cycles.
Detect cycles by checking for already visited nodes.
Check Connected Components:

After traversal, ensure all nodes are visited.
If true, the graph is a valid tree.
Return True if the graph is a valid tree; otherwise, return False.
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Undirected Graph Construction
        graph = defaultdict(set)
        for edge in edges:
            e0 = edge[0]
            e1 = edge[1]
            graph[e0].add(e1)
            graph[e1].add(e0)
        
        visited = [False] * n
        visited[0] = True
        q = deque([0])
        while q:
            curNode = q.popleft()
            
            for node in graph[curNode]:
                # Graph contains a cycle
                if visited[node]:
                    return False
                # Remove curNode from node's set so we don't cause a cycle ourselves
                graph[node].discard(curNode)
                # Add next node to our Queue
                q.append(node)
                # Mark the node visited
                visited[node] = True
        
        # Return True if all of the nodes that were visited are part of the same connected component
        return visited.count(True) == n
