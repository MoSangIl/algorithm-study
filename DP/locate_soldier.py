import sys

rl = lambda: sys.stdin.readline().rstrip()

n = int(rl())

soldiers = list(map(int, rl().split()))

soldiers.reverse()

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
print(dp)
