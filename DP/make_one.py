import sys
rl = lambda: sys.stdin.readline().rstrip()

n = int(rl())

dp = [0] * 30000
dp.append(0)
dp.append(1)

for i in range(2, n):
    # 처음 생각한 방법 1
    ## min 함수 인자가 많아져서 시간이 크고 / 변수를 위한 메모리를 사용한다.
    # d5 = 0
    # d3 = 0
    # d2 = 0
    # if (i + 1) % 5 == 0:
    #     d5 = (i + 1) // 5
    # if (i + 1) % 3 == 0:
    #     d3 = (i + 1) // 3
    # if (i + 1) % 2 == 0:
    #     d2 = (i + 1) // 2
    # m1 = i

    # ans = min(dp[d5 -1], dp[d3-1], dp[d2-1], dp[m1-1])
    # dp.append(ans + 1)

    # 답안지
    dp[i] = (i + 1) - 1
    if (i + 1) % 5 == 0:
        dp[i] = min(dp[i], dp[(i + 1) // 5])
    if (i + 1) % 3 == 0:
        dp[i] = min(dp[i], dp[(i + 1) // 3])
    if (i + 1) % 2 == 0:
        dp[i] = min(dp[i], dp[(i + 1) // 2])
    # 코드를 간편하게 줄이고, 연산또한 간단하게 할 수 있다.
print(dp[n-1])
