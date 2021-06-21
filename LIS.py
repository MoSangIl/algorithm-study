tc = int(input())

numbers = []

for _ in range(tc):
    n = int(input())

    numbers.append(list(map(int, input().split())))

def LIS(num_list):
    dp = [1] * len(num_list)

    for i in range(1, len(num_list)):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

for test_list in numbers:
    print(LIS(test_list))
