N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [ list() for i in range(N + 1) ] 
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

for i in range(1, N + 1):
    ans = str(i) + ": {" 
    for j in range(len(G[i])):
        if j >= 1:
            ans += ","
        ans += str(G[i][j])
    ans += "}"
    print(ans)
