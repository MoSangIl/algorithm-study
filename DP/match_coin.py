import sys

rl = lambda: sys.stdin.readline().rstrip()

n, price = map(int, rl().split())

coins = []
for _ in range(n):
    coins.append(int(rl()))

dp = [price] * (price + 1)

for i in range(1, price + 1):
    for coin in coins:
        if i == coin:
            dp[i] = 1
        elif i < coin:
            dp[i] = -1
        elif i > coin:
            remainder = i - coin
            if dp[remainder] != -1:
                dp[i] = min(dp[i], dp[remainder] + 1)
            else: dp[i] = -1

print(dp[price])
