tc = int(input())

numbers = []
for _ in range(tc):
    numbers.append(int(input()))

# Proper Divisor의 합이 N을 넘는다.
# 어떤 Subset의 합도 N이 될 수 없다.

def getProperDivisor(N):
    res = []
    for i in range(1, N // 2 + 1):
        if N % i == 0:
            res.append(i)
    return res

for N in tc:
    pdList = getProperDivisor(N)
    sumAll = sum(pdList)

    if sumAll > N:
        # Subset확인
        for i in pdList:
            subSum = sumAll - i
            if subSum == N:
                print('weird')
                break
            elif subSum < N:
                print('not weird')
    else:
        print('not weird')
