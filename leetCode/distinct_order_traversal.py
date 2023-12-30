g_nodes=5
g_from=[4,5,1,4,3]
g_to=[5,1,4,3,2]

adj=collections.defaultdict(set)
for i,j in zip(g_from,g_to):
    adj[i].add(j)
    adj[j].add(i)

visit,res,stack=set(),[],[-g_nodes]
heapq.heapify(stack)
while stack:    
    cur=-heapq.heappop(stack)
    if cur not in visit:
        visit.add(cur)
        res+=[cur]
        for kid in adj[cur]-visit:
            heapq.heappush(stack,-kid)
return res
