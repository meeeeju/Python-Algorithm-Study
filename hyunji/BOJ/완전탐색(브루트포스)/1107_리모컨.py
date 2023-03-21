import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
error=list(map(int,input().split()))

count=abs(100-N)

for num in range(1000001):
    num=str(num)
    for j in range(len(num)):
        if int(num[j]) in error:
            break
        elif j==len(num)-1:
            count=min(count,abs(int(num)-N)+len(num))
print(count)
