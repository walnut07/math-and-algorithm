# problem obtained from https://algo-method.com/tasks/307

N = int(input())
A = list(map(int, input().split()))

dp1 = 0 # will have the maximum number at the i-1th time
dp2 = 0 # will have the maximum number at the ith time

for i in range(1, N + 1):
    dp1 = dp2
    dp2 = max(dp1, dp1+A[i - 1])

print(max(dp1, dp2))