#시간초과나는 내 코드..
import sys
import math
input = sys.stdin.readline
def turn(t):
    if 0<t<=N: return t
    elif t<0: return N-(abs(N)%t)
    return abs(N-abs(t))
def bfs():
    same=dict()
    q=[]
    while queue:
        r,c,m,s,d = queue.pop(0)
        r = turn(r+(dir[d][0]*s))
        c = turn(c+(dir[d][1]*s))
        if (r,c) in same: 
            temp=[]+same[r,c]
            temp.append([m,s,d])
            same[r,c]=temp
        else: same[r,c]=[[m,s,d]]
    for key,value in same.items():
        # print(key,value)
        if len(value)>=2:
            m,s=0,0
            even = True; odd = True;
            for i in range(len(value)):
                m+=value[i][0]
                s+=value[i][1]
                if value[i][2]%2==0 and odd==True: odd=False
                elif value[i][2]%2!=0 and even==True: even=False
            if math.floor(m/5)!=0:
                if odd or even: start=0
                else: start=1
                for i in range(0,7,2):
                    q.append([key[0],key[1],math.floor(m/5),math.floor(s/len(value)),start+i])
        else: q.append([key[0],key[1],value[0][0],value[0][1],value[0][2]])
    return q
            
            
N,M,K = map(int,input().split()) # 칸 수, 파이어볼 수, 이동 수
dir = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
fireball = [[[] for _ in range(N+1)] for _ in range(N+1)]
queue=[]
for _ in range(M):
    r,c,m,s,d = map(int,input().split()) # (위치),질량, 속력, 방향
    # fireball[r][c].append([m,s,d]) # 질량, 속력, 방향
    queue.append([r,c,m,s,d]) # 질량, 속력, 방향 
# print(*fireball)
for _ in range(K):
    queue=bfs()
    # print(*queue)
result=0
for i in range(len(queue)):
    result+=queue[i][2]
print(result)
