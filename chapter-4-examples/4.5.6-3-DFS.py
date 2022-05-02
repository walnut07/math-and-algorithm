import sys

N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# adjacency list
G = [ list() for _ in range(N + 1) ]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# DFS
sys.setrecursionlimit(10000)
def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

visited = [ False ] * (N + 1)
dfs(1, G, visited)

# output the ans
## output "Yes" if the graph is connected
ans = "Yes"
for i in range(1, N + 1):
    if visited[i] == False:
        ans = "No"
print(ans)