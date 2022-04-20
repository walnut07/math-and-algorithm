## time taken: 50 minutes
## reflection
# - forgot to devide cnt[50000] * ( cnt[50000] -1 ) by 2
#    - choose 2 cards from cnt[50000], can be represented as cnt[50000] C 2 
#    - so need to devide by 2

import math
N = int(input())
A = list(map(int, input().split()))
LIMIT = 100000
cnt = {}
ans = 0

for i in range(LIMIT):
    cnt[i] = 0

for i in range(N):
    cnt[A[i]] += 1

for i in range(1, LIMIT):
    ans += cnt[i] * cnt[LIMIT-i]

ans += cnt[LIMIT] * ( cnt[LIMIT] -1 ) // 2

print(ans)
