#계속 시간초과나서 pypy로 돌림,,
#메모리:259740 시간:520ms
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
liist=list(map(int,input().split()))

start=1
end=max(liist)

while start<=end:
    middle=(start+end)//2
    tree=0
    
    for i in liist:
        if i>=middle:
            tree+=i-middle
    
    if tree>=M:
        start=middle+1
    else:
        end=middle-1
print(end)
    
