import sys

input = sys.stdin.readline
 
n = int(input()) 
data = list(map(int,input().split())) 

#최대값 저장 변수
ans=0

#i번째 원소까지의 누적합
sum=[] 
sum.append(data[0]) 

for i in range(1,n): 
    sum.append(sum[i-1]+data[i]) 
    
    
#case1 - left
for i in range(1,n-1): 
    ans=max(ans,sum[n-2]+sum[i-1]-data[i])
    #왼쪽 끝에 벌통
    #오른쪽 끝에 벌1, i번쨰 위치에 벌2
 
#case2 - right
for i in range(1, n-1): 
    ans = max(ans, sum[n-1] - data[0] - data[i] + sum[n-1] - sum[i]) 
    #오른쪽 끝에 벌통
    #왼쪽 끝에 벌1, i번째 위치에 벌2
   
#case3 - middle
for i in range(1,n-1): 
    ans=max(ans,sum[n-2] - data[0] + data[i])
    #왼쪽 끝에 벌1, 오른쪽 끝에 벌2
    #i번째 위치에 벌통
       