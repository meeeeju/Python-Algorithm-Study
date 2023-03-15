#블로그참고
# 42340 KB / 220 ms
import sys
N=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))

for i in range(N-2,-1,-1):  # 누적합 누하기 
    nlist[i]+=nlist[i+1]

result=0  

# 벌벌꿀
for i in range(1,N-1):
    result=max(result,nlist[i+1]*2+(nlist[1]-nlist[i]))

# 벌꿀벌
for i in range(1,N-1):
    result=max(result,(nlist[1]-nlist[i+1])+(nlist[i]-nlist[-1]))

# 꿀벌벌
for i in range(N-2,-1,-1):
    result=max(result,(nlist[0]-nlist[i])*2+(nlist[i+1]-nlist[-1]))
print(result)
    
