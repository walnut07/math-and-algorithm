N = int(input())
A = list(map(int, input().split())) # distance
M = int(input()) # where they stop traveling
B = [ None ] * M # their route

for i in range(M):
    num = int(input())
    B[i] = num

#cumulative sum
C = [ 0 ] * ( N ) #N = A + 1
C[0] = 0
for i in range(1, N):
    C[i] = C[i - 1] + A[i - 1]

ans = 0
for i in range(M - 1):
    if C[B[i] - 1] < C[B[i + 1] - 1]:
        ans +=  ( C[B[i + 1] - 1] ) - ( C[B[i] - 1] )
    else:
        ans +=  ( C[B[i] - 1] ) - ( C[B[i + 1] - 1])

print(ans)