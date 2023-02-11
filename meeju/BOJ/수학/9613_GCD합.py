# 44ms / 31256KB
import sys
input =sys.stdin.readline

t = int(input()) # 테스트 케이스의 수
gcd = 0 
gcd_list = []

for _ in range(t):
    integer_list=list(map(int,input().split()))
    n = integer_list.pop(0)     # 수의 갯수
    integer_list.sort(reverse=True)
    for i in range(len(integer_list)-1):
        for j in range(i+1, len(integer_list)):
            r = 1
            x = integer_list[i]
            y = integer_list[j]

            while(r):      # gcd 로직
                r = x % y
                x = y
                y = r
            gcd += x
            
    gcd_list.append(gcd)
    gcd =0

for result in gcd_list:
    print(result)
            


    