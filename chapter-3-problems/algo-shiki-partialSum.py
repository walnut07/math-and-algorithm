#Problem obtained from https://algo-method.com/tasks/310/editorial

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * ( M + 1 ) for i in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if j < A[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else: 
            if j == dp[i - 1][j - A[i - 1]] + A[i - 1]:
                dp[i][j] += 1
            else:
                dp[i][j] = dp[i - 1][j - A[i - 1]] + dp[i- 1][j]
            

for i in range(N + 1):
    print(dp[i]) 