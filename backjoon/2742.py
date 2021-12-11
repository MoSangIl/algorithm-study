import sys 

rl = lambda: sys.stdin.readline().rstrip()

N = int(rl())

for i in range(N):
    print(N - i)

# N = range(int(input()), 0, -1)
# print("\n".join(map(str,N)))

# print("3".join(['ee','aa','aa'])) 
# > ee3aa3aa
# join 함수
## str.join(*iterable) -> str을 사잇값으로 배열 값을 하나의 문자열로 붙임

