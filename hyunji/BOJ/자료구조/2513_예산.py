#블로그 참조
#메모리 :32276 시간 :76ms
import sys
input=sys.stdin.readline
N=int(input())
money=list(map(int,input().split()))
max_money=int(input())

summ=0
count=0

money.sort()
start=0
end=money[-1]

for i in range(N):
    summ+=money[i]

if summ<=max_money:
    print(money[-1])

else:
    while start<=end:
        middle=(start+end)//2
        
        summ=0
        
        for i in money:
            if i>middle:
                summ+=middle
            else:
                summ+=i
                
        if summ>max_money:
            end=middle-1
        else:
            start=middle+1
    print(end)
