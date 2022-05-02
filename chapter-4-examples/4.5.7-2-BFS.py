import queue

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

# initilization
dist = [ -1 ] * (N + 1)
dist[1] = 0
Q = queue.Queue()
Q.put(1)

while not Q.empty():
    pos = Q.get()
    for i in G[pos]:
        if dist[i] == -1:
            dist[i] = dist[pos] + 1
            Q.put(i)

# output the answer       
for i in range(1, N + 1):
    print(dist[i])



