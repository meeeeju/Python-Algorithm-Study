# 31256kb /	252ms
import sys
input = sys.stdin.readline

'''
9
BOJBOJBOJ'''

N = int(input())    # 보드블럭의 갯수
road = input().rstrip()     # 거리 

energy = [float('inf') for _ in range(N)]
energy[0]=0

for i in range(N-1):
    for j in range(i+1,N):
        if road[i]=='B':
            if road[j]=='O':
                energy[j]= min(energy[j],energy[i]+ (j-i)*(j-i))
        if road[i]=='O':
            if road[j]=='J':
                energy[j]= min(energy[j],energy[i]+ (j-i)*(j-i))
        if road[i]=='J':
            if road[j]=='B':
                energy[j]= min(energy[j],energy[i]+ (j-i)*(j-i))

if energy[-1]==float('inf'):    # 한번도 업데이트 된 적이 없다면 
    print(-1)
else:
    print(energy[-1])

