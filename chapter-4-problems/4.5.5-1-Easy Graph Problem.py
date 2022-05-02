import sys
sys.setrecursionlimit(100000000)

# input
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split()) 

# adjacency list
G = [ list() for _ in range( N + 1 ) ] # O(N)
for i in range(M): # O(M)
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

ans = 0
for i in range(1, N + 1): #worst case complexity: O(N^2)
    count = 0
    for j in G[i]:
        if i > j:
            count += 1
    if count == 1:
        ans += 1

print(ans)

