# Problem obtained from https://algo-method.com/tasks/314

S = input()
T = input()

S_list = []
T_list = []


for i in range(len(S)):
    S_list.append(S[i])

for i in range(len(T)):
    T_list.append(T[i])

dp = [ [None] * ( len(S) + 1 )  for i in range(len(T) + 1)]

for i in range(0, len(S) + 1):
    dp[0][i] = 0

for i in range(0, len(T) + 1):
    dp[i][0] = 0


for i in range(1, len(S) + 1): #abc, range(1, 2, 3)
    for j in range(1, len(T) + 1): #ab, range(1, 2, 3)
        if S_list[i - 1] == T_list[j - 1]:
            dp[j][i] = dp[j-1][i-1] + 1
            #S_list[i - 1] = "#"
            print(S_list)
        else:
            dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

        
print(dp[len(T)][len(S)])
#for i in range(len(T)+1):
    #print(dp[i])
