#메모리 : 33376 / 시간 : 1520ms
import math
N=int(input())

def sosoo(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

for i in range(N):
    n=int(input())
    while True:
        if sosoo(n):
            print(n)
            break
        else:
            n=n+1
