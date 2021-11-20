# 좌표가 어느 사분면에 위치하는 지 출력

def main() :
    
    x = int(input())
    y = int(input())
    
    if x * y > 0:
        if x > 0:
            print(1);
        else:
            print(3)
    else:
        if x > 0:
            print(4)
        else:
            print(2)

if __name__ == "__main__":
    main()