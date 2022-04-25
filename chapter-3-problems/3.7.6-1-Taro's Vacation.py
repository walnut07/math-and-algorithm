N = int(input())
A = list(map(int, input().split()))

#一次元配列を２つつくる
dp1 = [None] * (N + 1) #i日目に勉強した場合の最大学力
dp2 = [None] * (N + 1) #i日目に勉強しなかった場合の最大学力

dp1[0] = 0
dp2[0] = 0

for i in range(1, N+1):
    dp1[i] = dp2[i - 1] + A[i - 1]
    dp2[i] = max(dp1[i - 1], dp2[i - 1])

print(max(dp1[N], dp2[N]))

