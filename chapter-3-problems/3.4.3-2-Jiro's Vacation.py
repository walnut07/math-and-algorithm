# total taken : 20 minutes
# got wrong answers because not applying "max" function when assigning a value to dp2[i]
# dp1 is the array that has the maximum value when studied on the ith day
# dp2 is the array that has the maximum value when NOT studied on the ith day

N = int(input())
A = list(map(int, input().split()))

dp1 = [ None ] * ( N + 1 ) # when studied on the ith day
dp2 = [ None ] * ( N + 1 ) # when not studied on the ith day

dp1[0] = 0
dp2[0] = 0

for i in range(1,  N + 1 ):
    dp1[i] = dp2[ i - 1 ] + A[ i - 1 ]
    #print(dp1[i])
    dp2[i] = max( dp1[ i - 1 ], dp2[ i - 1 ])
    #print(dp2[i])

print(max(dp1[N], dp2[N]))