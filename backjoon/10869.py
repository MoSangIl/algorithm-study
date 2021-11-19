def main() :
    # int 클래스의 일종이다. 
    # number, string to int or 0
    a, b = map(int, input().split())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)

if __name__ == "__main__":
    main()