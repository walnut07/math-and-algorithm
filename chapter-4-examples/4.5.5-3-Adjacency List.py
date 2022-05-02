#Implemented by myself

N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# create an adjacencey list
X = [ list() for _ in range(N + 1) ]
for i in range(M):
    X[A[i]].append(B[i])
    X[B[i]].append(A[i])

# output the adjacency list
for i in range(1, N + 1):
    ans = str(i) + ": { "
    for j in range(len(X[i])):
        ans += str( X[i][j] )
        if j < ( len(X[i]) - 1 ):
            ans += ", "
    ans += " }"
    print(ans)




