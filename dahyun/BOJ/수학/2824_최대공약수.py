# 76ms / 33376KB
import sys
import math
#재귀함수
# def gcd(x,y):
#     if y==0 : return x
#     else : return gcd(y,x%y)

#유클리드
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
    
N=int(sys.stdin.readline())
ns=math.prod(list(map(int,sys.stdin.readline().split()))) # A 값
M=int(sys.stdin.readline())
ms=math.prod(list(map(int,sys.stdin.readline().split()))) # B 값


result= gcd(max(ns,ms),min(ns,ms))  # 인자로 (작은 값, 큰 값)
if len(str(result))>9: print(str(result)[-9:]) # 길이가 9 이상이면 9개만 출력
else: print(result)
