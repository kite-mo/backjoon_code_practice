import sys

# sys.stdin = open('./test.txt')

N = int(sys.stdin.readline())
rgb_prices = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]
dp = [[0] * 3 for i in range(N)]
R, G, B = 0, 1, 2
dp[0][R] = rgb_prices[0][R]
dp[0][G] = rgb_prices[0][G]
dp[0][B] = rgb_prices[0][B]

for i in range(1, N):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + rgb_prices[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + rgb_prices[i][G]
    dp[i][B] = min(dp[i-1][G], dp[i-1][R]) + rgb_prices[i][B]

print(min(dp[-1]))