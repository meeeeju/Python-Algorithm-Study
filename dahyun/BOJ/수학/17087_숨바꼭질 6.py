# 42176 KB / 112 ms
import sys
def gcd(x,y):  # 유클리드 호제법
    while y!=0:
        x,y=y,x%y
    return x
N,S = map(int,sys.stdin.readline().split())  # N : 자연수 , S : 언니 위치
A_list = list(map(int,sys.stdin.readline().split()))  # nlist : 동생들 위치
result=0
for i in range(len(A_list)) :  # 언니위치와 동생 위치의 차이 값의 최대공약수 구하면 됨 !
    if i>=1:  result=gcd(result,abs(A_list[i]-S))
    else : result=abs(A_list[i]-S)
print(result)
    
