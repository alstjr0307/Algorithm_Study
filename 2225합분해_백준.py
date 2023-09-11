n, k = map(int,input().split())
dp = [0 for _ in range(n+1)]
dp[0]=1
dp[1]=k
dp[2] = 