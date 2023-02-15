#블로그 참조
#메모리 : 33508 시간 : 88ms
from math import sqrt
N,M=map(int,input().split())

arr=[input().rstrip() for _ in range(N)]

result=-1

for i in range(N): #시작 행
    for j in range(M): #시작 열
        for a in range(-N,N): #행 등차
            for b in range(-M,M): #열 등차
                
                num=''
                y,x=i,j
                
                while 0<=y<N and 0<=x<M: 
                    num+=arr[y][x]
                    if a==0 and b==0:
                        break # 둘 다 공차가 0이면 break 빠져나옴
                    if int(sqrt(int(num)))**2==int(num): #제곱수인지 판별
                        result=max(int(num),result)
                    y+=a
                    x+=b
print(result)
