from collections import deque

def bfs(adj,s):
    visited = [False]*len(adj)
    q = deque([s])
    visited[s] = True
    while q:
        curr = q.popleft()
        print(chr(curr + ord("A")),end=" ")
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
    
# example 
V = 7
adj =[[] for _ in range(V)]
edge = [(0,1),(0,2),(0,6),(2,3),(2,4),(2,5),(6,5)]
for u,v in edge:
    add_edge(adj,u,v)
    
print("BFS starting for 0:")
bfs(adj,0)
