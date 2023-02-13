#'블로그 참조
#메모리 : 31256 시간  : 44ms
N,M=map(int,input().split())

def GCD(N,M):
    for i in range(N,0,-1):
        if N%i==0:
            if M%i==0:
                return i

if N<M:
    print(M-GCD(N,M))
else:
    N=N%M
    if N==0:
        print(N)
    else:
        
        print(M-GCD(N,M))
'''
from fractions import Fraction
N,M=map(int,input().split())

m=1
count=0

if N<M:
    n=Fraction(N,M)
    while m>0:
        m=m-n
        if m>=0:
            count+=1
    
    if m==0:
        print((count-1)*N)
    else:
        print(count*N)
else:
    N=N%M
    n=Fraction(N,M)
    if N==0:
        print(N)
    else:
        while m>0:
            m=m-n
            if m>=0:
                count+=1
        
        if m==0:
            print((count-1)*N)
        else:
            print(count*N)'''
