# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 配列の初期化
dp = [ [ None ] * (S + 1) for i in range(N + 1) ] 
 #y=カードを取る枚数N枚までの場合 x=とったカードの合計
dp[0][0] = True #カードを取る枚数が0枚なら合計は0枚
for i in range(1, S + 1): #カードを取る枚数が0枚なら合計は1以上にならないため
	dp[0][i] = False

# 動的計画法
for i in range(1, N+1): #0枚とった場合は8行目でTrue/Falseを分けているため、1からN+１まで
    for j in range(0, S+1):
        if j < A[i - 1]:
			# j < A[i-1] のとき、カード i を選べない
		    dp[i][j] = dp[i - 1][j]
		else:
			# j >= A[i-1] のとき、選ぶ / 選ばない 両方の選択肢がある
			if (dp[i - 1][j] == True or dp[i - 1][j - A[i - 1]] == True):
				dp[i][j] = True
			else:
				dp[i][j] = False


# 答えを出力