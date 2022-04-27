#自分で実装したコード
N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [ None ] * Q
R = [ None ] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())

#累積和を計算する
B = [ None ] * ( N + 1 ) #0日目, 来場者0人も含む
B[0] = 0
for i in range(1, N + 1):
    B[i] = B[i - 1] + A[i - 1]

#L[i]日目からR[i]日目までの合計来場者数を計算する
ans = [ None ] * Q
for i in range(Q):
    ans[i] = B[R[i]] - B[L[i] - 1]

for i in range(Q):
    print(ans[i])