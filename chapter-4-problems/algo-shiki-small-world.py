# input
import queue


N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# create adjacency list
G = [ list() for _ in range(N) ]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# Breadth First Search
Q = queue.Queue()
Q.put(0)
dist = [ -1 for _ in range(N) ]
dist[0] = 0

while not Q.empty():
    pos = Q.get()
    for node in G[pos]:
        if dist[node] == -1:
            dist[node] = dist[pos] + 1
            Q.put(node)

print(max(dist))


# python3 algo-shiki-small-world.py 