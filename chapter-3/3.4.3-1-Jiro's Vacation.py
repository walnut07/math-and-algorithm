# time taken: 5 minutes
# reflection
## I understand expectation well

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += ( 2 / 6 ) * A[i] + ( 4 / 6 ) * B[i]

print(ans)