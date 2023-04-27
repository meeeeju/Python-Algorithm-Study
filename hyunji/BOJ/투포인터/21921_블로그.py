#계속 시간 초과 남,,
import sys
input=sys.stdin.readline

N,X=map(int,input().split())
liist=list(map(int,input().split()))
count=0
maxx=0
end=0

for i in range(N):
    summ=0
    end=i
    while end-i<X and end<N:
        summ+=liist[end]
        end+=1
    if end-i==X:
        if summ>maxx:
            count=1
            maxx=summ
        elif summ==maxx:
            count+=1

if maxx==0:
    print("SAD")
else:
    print(maxx)
    print(count)            
    

