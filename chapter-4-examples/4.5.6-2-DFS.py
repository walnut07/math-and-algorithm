import sys

N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

sys.setrecursionlimit(10000000)

# adjacency list
G = [ list() for _ in range(N + 1) ]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# define a function 
def DFS(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            DFS(i, G, visited)
        
visited = [ False ] * ( N + 1 )
DFS(1, G, visited)

# output the answer
ans = "The graph is connected"
for i in range(1, N + 1):
    if visited[i] == False:
        ans = "The graph is NOT connected"




