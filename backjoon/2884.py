# 45분 빠른 알람 설정
def main() :
    
    h, m= map(int, input().split())
    
    # m > 45
    ## h 는 변경하지 않는다.
    # m < 45 
    ## h = 0
    ### h = 23
    ## h >= 0
    ### h = h - 1
    ## m = m + 60 - 45
    if m >= 45:
        print(h, m - 45)
    else:
        print(23, end=" ") if h == 0  else print(h - 1, end=" ")
        print(m+60 - 45)
        

if __name__ == "__main__":
    main()