# 34324 KB / 480 ms
import sys
input = sys.stdin.readline
def bfs():
    same=dict()
    q=[]
    while queue:
        r,c,m,s,d = queue.pop(0)
        r, c = (r+dir[d][0]*s)%N,(c+dir[d][1]*s)%N
        if (r,c) in same: same[(r,c)].append([m,s,d])
        else: same[(r,c)]=[[m,s,d]]
    for key,value in same.items():
        if len(value)>=2:
            m,s=0,0 # 총질량, 총속력
            even = True; odd = True;
            for i in range(len(value)):
                m+=value[i][0]
                s+=value[i][1]
                if value[i][2]%2==0 and odd==True: odd=False
                elif value[i][2]%2!=0 and even==True: even=False
            if m//5!=0:
                if odd or even: start=0
                else: start=1
                for i in range(0,7,2):
                    q.append([key[0],key[1],m//5,s//len(value),start+i])
        else: q.append([key[0],key[1],value[0][0],value[0][1],value[0][2]])
    return q
            
            
N,M,K = map(int,input().split()) # 칸 수, 파이어볼 수, 이동 수
dir = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
queue=[]
for _ in range(M):
    r,c,m,s,d = map(int,input().split()) # (위치),질량, 속력, 방향
    queue.append([r,c,m,s,d]) # 질량, 속력, 방향 
for _ in range(K):
    queue=bfs()
result=0
for i in range(len(queue)):
    result+=queue[i][2]
print(result)
