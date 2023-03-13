# 31256 KB / 44 ms
import sys
input=sys.stdin.readline
count=0
level_list=[]
N=int(input())
for i in range(N):
    level_list.append(int(input()))
for i in range(N-1,0,-1): # 뒤에서부터 앞으로
    if level_list[i-1]>=level_list[i]: # 현재 숫자보다 앞의 숫자가 더 크다면 앞의 숫자 줄이기
        count+=level_list[i-1]-level_list[i]+1
        level_list[i-1]-=level_list[i-1]-level_list[i]+1
       
print(count)
        
    
