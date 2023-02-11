#33376KB / 2356ms
import sys
import math
for _ in range(int(sys.stdin.readline())):
    n =int(sys.stdin.readline()) 
    
    while True:
        for i in range(2,int(math.sqrt(n))+1): # 소수인지 확인
            if n%i==0 : break
        else : 
            if n!=1 and n!=0:  # n이 1 또는 0이 아니라면 출력
                print(n)
                break
        n+=1 # n 증가
