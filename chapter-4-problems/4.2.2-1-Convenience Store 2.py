T = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

# difference
B = [ 0 ] * ( T + 1 )

for i in range(N):
    B[ L[i] ] += 1
    B[ R[i] ] -= 1

# output the ans
ans = [ 0 ] * ( T )
ans[0] = B[0]
for i in range(1, T):
    ans[i] = ans[i - 1] + B[i]

for i in range( T ):
    print(ans[i])

