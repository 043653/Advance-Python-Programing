
def min_cost_path(cost):
    m = len(cost)
    n = len(cost[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = cost[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = cost[i][j] + min(
                dp[i-1][j],      
                dp[i][j-1],      
                dp[i-1][j-1]     
            )

    return dp[m-1][n-1]


cost = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

result = min_cost_path(cost)

print("Minimum cost path:", result)
