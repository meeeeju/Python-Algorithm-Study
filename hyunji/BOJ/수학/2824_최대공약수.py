#메모리 : 33376 시간 : 80 ms
#유클리드 호제법 블로그 찾아봄
import math

N=int(input())
NN=map(int,input().split())
M=int(input())
MM=map(int,input().split())

A=math.prod(NN)
B=math.prod(MM)

n=min(A,B)
k=max(A,B)


def GCD(n,k):
    while k>0:
        n,k=k,n%k
    return n

print(str(GCD(n,k))[-9:])
