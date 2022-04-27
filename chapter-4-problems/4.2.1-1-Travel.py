N = int(input())
A = list(map(int, input().split())) # distance
M = int(input()) # where they stop traveling
B = [ None ] * M # their route

for i in range(M):
    num = int(input())
    B[i] = num

#cumulative sum
CM = [ 0 ] * ( N )
CM[0] = A[0]
for i in range(1, N):
    CM[i] = CM[i - 1] + A[i - 1]

ans = 0
for i in range(M - 1):
    if B[i] < B[i + 1]:
        ans += CM[ B[i + 1] - 1 ] - CM[ B[i] - 1 ]
    else:
        ans += CM[B[i] - 1] - CM[B[i + 1] - 1]

print(ans)