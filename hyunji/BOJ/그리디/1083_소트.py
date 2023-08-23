import sys
input=sys.stdin.readline
n=int(input())
liist=list(map(int,input().split()))
s=int(input())
count=0
liist_ex=liist
liist_ex=sorted(liist_ex,reverse=True)
check=sorted(liist_ex,reverse=True)
line=0

result=[]

for _ in range(n):
    for i in range(n):
        if count==s:
            result=liist
            #print(*liist)
            break
        flag=0
        for j in range(n):
            if liist[j]==check[j]:
                flag+=1
        if flag==len(liist):
            result=liist
            break
        
        if liist[i]==max(liist_ex):
            if i-line<=s-count:
                for j in range(i,line,-1):
                    liist[j],liist[j-1]=liist[j-1],liist[j]
                    count+=1
                    #print(liist)
                line+=1
                del(liist_ex[0])
                break
            else:
                #count+=1
                del(liist_ex[0])
                break
        
lastcount=0   
lastresult=[]         
if len(result)==0:
        
    for i in range(1,n):
        if liist[i-1]<liist[i]:
            liist[i-1],liist[i]=liist[i],liist[i-1]
            lastcount+=1
            if lastcount==s:
                lastresult=liist
                break
        else:
            continue
    print(*lastresult)
else:    
    print(*result)
    
