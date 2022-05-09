import sys
sys.setrecursionlimit(10000)

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

# depth first search
def dfs(pos, col, G):
    for vertex in G[pos]:
        if col[vertex] == -1:
            col[vertex] = 1 - col[pos]
            dfs(vertex, col, G)
    return col

def examineIfBigraph(col, A, B):
    ans = "Yes, it is a bigraph"
    for i in range(1, M):
        if col[A[i]] == col[B[i]]:
            ans = "No, it isn't a bigraph"
            return ans
    return ans

col = [ -1 for _ in range(N + 1) ]
col[1] = 1
pos = 1
new_col = dfs(pos, col, G)
print(new_col)
print(examineIfBigraph(new_col, A, B))

# python3 "4.5.7-2-Bipartite Graph.py"
# 3 2
# 1 2
# 1 3