N = int(input())
Q = int(input())
L = [ None ] * Q
R = [ None ] * Q
X = [ None ] * Q

for i in range(Q):
    L[i], R[i], X[i] = map(int, input().split())

B = [ 0 ] * ( N + 1 )
for i in range(Q):
    B[L[i] - 1] += X[i]
    B[R[i]] -= X[i]

#階差から大小関係を計算する
ans = ""
for i in range(1, N):
    if B[i] < 0:
        ans += ">"
    elif B[i] > 0:
        ans += "<"
    elif B[i] < 0:
        ans += "="

print(ans)