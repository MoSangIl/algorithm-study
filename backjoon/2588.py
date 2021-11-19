
def main() :
    # int 클래스의 일종이다. 
    # number, string to int or 0
    a = int(input())
    b = int(input())
    
    print(a * (b % 10)) # 1 의자리와 곱
    print(a * ((b % 100) // 10))
    print(a * (b // 100))
    print(a * b)


if __name__ == "__main__":
    main()