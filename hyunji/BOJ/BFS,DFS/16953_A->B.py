A,B=map(int,input().split())
count=0

while (B!=A):
    temp=B
    if B%2==0:
        B=B//2
        count+=1
        
    elif B%10==1:
        B=B//10
        count+=1
        
    if temp==B:
        print(-1)
        break

else:
    print(count+1)
