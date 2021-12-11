
tc = int(input())

tc_num =[]
for i in range(tc):
    num = []
    a, b, c, a1, b1, c1 = map(int, input().split())
    num.append(a)
    num.append(b)
    num.append(c)
    num.append(a1)
    num.append(b1)
    num.append(c1)
    tc_num.append(num)

for data in tc_num:
    distance = (data[0] - data[3]) ** 2 + (data[1] - data[4]) ** 2
    if distance == 0:
        if data[2] == data[5]: 
            print(-1)
        else:
            print(0)
        continue
    two_rad_sum = (data[2] + data[5]) ** 2
    two_rad_dif = (data[2] - data[5]) ** 2
    if distance == two_rad_sum :
        print(1)
    elif distance < two_rad_sum :
        if distance == two_rad_dif:
            print(1)
        elif distance < two_rad_dif:
            print(0)
        else:
            print(2)
    elif distance > two_rad_sum :
        print(0)