#블로그 참고
#메모리 :42340 시간 :532ms
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
liist=list(map(int,input().split()))
start=max(liist)
end=sum(liist)

while start<=end:
    middle=(start+end)//2
    count=1
    size=0

    for i in liist:
        if (size+i)<=middle:
            size+=i
        else:
            size=i
            count+=1
    if count<=M:
        end=middle-1
    else:
        start=middle+1
print(start)

