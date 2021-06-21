import sys

rl = lambda : sys.stdin.readline().rstrip()
# tc = int(input())
tc = int(rl())
testcase = []
for i in range(tc):
    # size = int(input())
    size = int(rl())
    game_table = []
    for row in range(size):
        # game_table.append(list(map(int, input().split())))
        game_table.append(list(map(int, rl().split())))
    testcase.append([game_table, size])

for TC in testcase:
    table = TC[0]
    n = TC[1]
    path = [[0] * n for _ in range(n)]

    path[0][0] = 1

    for i in range(n):
        for row in range(i+1):
            for col in range(i+1):
                # 1 인지 확인
                if path[row][col] == 1:

                    # 해당 열에서 값을 사용하여 오른쪽 혹은 아래로 이동
                    val = table[row][col]
                    # 벗어날 경우 아웃
                    # 안 벗어나면 1 체크
                    # 아래
                    if row + val <= i:
                        path[row + val][col] = 1
                    # 오른쪽
                    if col + val <= i:
                        path[row][col + val] = 1
    if path[n - 1][n - 1] == 1:
        print("YES")
    else:
        print("NO")
