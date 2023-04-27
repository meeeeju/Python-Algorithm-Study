#end지정하는거 블로그참고
#메모리 :38984 시간 :432
import sys
input=sys.stdin.readline
N,C=map(int,input().split())
liist=[]
for i in range(N):
    liist.append(int(input()))
liist.sort()

start=1
end=liist[-1]-liist[0]
summ=0

if N==2:
    print(liist[-1]-liist[0])
else:
    while start<=end:
        middle=(start+end)//2
        count=1
        cur=liist[0]

        for i in liist:
            if i-cur>=middle:
                count+=1
                cur=i
        if count>=C:
            start=middle+1
            summ=middle
        else:
            end=middle-1
    print(summ)
