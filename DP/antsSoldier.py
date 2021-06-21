# 1 각 케이스를 저장한 후 최댓값을 고른다.

num = int(input())
food_house = input().split(' ')

food_house = list(map(int, food_house))

foods_acc = []
for i in range(num - 2):
    for j in range(i + 2, num):
        foods_acc.append(food_house[i] + food_house[j])


maxV = foods_acc[0]
for n in foods_acc:
    if maxV < n:
        maxV = n

print(maxV)

# 위 경우는 2개만 선택한다고 한 가정.. 멍청 함 멍멍
