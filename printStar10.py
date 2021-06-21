def f(n):
    # 줄의 총 개수
    for i in range(n):
        # 각줄마다의 출력
        for j in range(n):
            # 전체를 3등분했을 때 1층 과3층 출력 정의
            if i / (n/3) != 1:
                printLine(n, i, j)
            # 2층 출력 정의
            else:
                # 2층 한 줄을 3등분 했을 때 가운데 부분 출력 정의
                if j / (n/3) == 1:
                    print(" ", end='')
                else:
                    printLine(n, i, j)
    # 한 줄 입력 후 한칸 띄우기
    print('')


def printLine(n, i, j):
    # 모든 n줄에서 3묶음, 9묶음, 27묶음... 씩 했을때 가운데 줄 정의 & & 한 줄에서 별을 3묶음씩 했을떄 가운데 부분 정의
    if n > 3:
        if (i/(n/9)) % 3 == 1 and (j/(n/9)) % 3 == 1:
            print(" ", end='')
        else:
            printLine(n/3, i, j)
            if n == 9:
                print("*", end='')


n = int(input())

f(n)
