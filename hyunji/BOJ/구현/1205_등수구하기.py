#메모리 :31256 시간 :44ms
import sys
input=sys.stdin.readline

N,new,P=map(int,input().split())
n=list(map(int,input().split()))

if N==0:
    print(1)
else:
    n.append(new)
    n.sort(reverse=True)
    
    if len(n)<=P:
        print(n.index(new)+1)
    else:
        if n[-1]!=new:
            print(n.index(new)+1)
        else:
            print(-1)
