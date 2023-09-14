k, n = map(int,input().split())
data=[1 for _ in range(k+1)]
dp=[[1 for i in range(k+1)] for _ in range(n+1)]

for i in range(2, n+1):
    for j in range(k+1):

        dp[i][j] = sum(dp[i-1][0:j+1])
print(dp[n][k]%1000000000)