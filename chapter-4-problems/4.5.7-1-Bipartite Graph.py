# Took 60 minutes.
# Saw hints when got stuck with definiting the examineBipartite function


import sys
# input
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# adjacency list
G = [ list() for _ in range(N + 1) ]
for i in range(M):
    G[A[i]].append(B[i])
    print(A[i])    
    print(B[i])
    G[B[i]].append(A[i])

# Breadth First Search
color = [ -1 ] * ( N + 1 )
color[1] = 1 # colors are 1 or 0. -1 means unvisited.

sys.setrecursionlimit(10000)
def examineBipartite(pos, G, color):
    for i in G[pos]:
        # Not visited
        if color[i] == -1:
            if color[pos] == 1:
                color[i] = 0
                examineBipartite(i, G, color)
            elif color[pos] == 0:
                color[i] = 1
                examineBipartite(i, G, color)
        # Visited
        if color[i] != -1:
            if color[i] == color[pos]:
                return "No"
            elif  color[i] != color[pos]:
                continue 

examineBipartite(1, G, color)
print(color)

# Examine if adjacency nodes have a different color
ans = "Yes"
for i in range(M):
    if color[A[i]] == color[B[i]]:
        ans = "No"
print(ans)

        



