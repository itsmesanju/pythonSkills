"""
Create a directed graph (graph) and an indegree dictionary based on the given prerequisites.
Initialize an empty list res to store the order of courses.
Initialize a deque (que) with courses that have an indegree of 0 (no prerequisites).
While the deque is not empty:
Pop a course from the deque.
Append the course to the result list.
Update the indegree of neighboring courses and enqueue those with an indegree of 0.
Check if the length of the result list is equal to the total number of courses. If true, return the result list; otherwise, return an empty list.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = defaultdict(int)
        for c,p in prerequisites:
            graph[p].append(c)
            indegree[c]+=1
        res = []
      que = deque()

      for i in range(numCourses):
          if indegree[i] == 0:
              que.append(i)
            
      while que:
            node = que.popleft()
            res.append(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    que.append(neigh)
        if len(res)==numCourses:
            return res
        return []
        
