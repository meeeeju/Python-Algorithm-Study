#1퍼에서 자꾸만 틀려서 내 코드 참고!
# 33300KB/	452ms
import sys
input = sys.stdin.readline
def bfs():
    same={}
    while queue:
        r,c,m,s,d = queue.pop(0)
        r,c = (r+dir[d][0]*s)%N,(c+dir[d][1]*s)%N
        if (r,c) in same:
            same[(r,c)].append([m,s,d])
        else: same[(r,c)]=[[m,s,d]]
    q=[]
    for key,value in same.items():
        if len(value)>=2:
            rm,rs,rd=0,0,True
            even = True; odd = True;
            for m,s,d in value:
                rm+=m;rs+=s;
                if d%2==0 and odd==True: odd=False
                elif d%2!=0 and even==True: even=False
            rm//=5
            rs//=len(value)
            if rm!=0:
                if even or odd:
                    q.append([key[0],key[1],rm,rs,0])
                    q.append([key[0],key[1],rm,rs,2])
                    q.append([key[0],key[1],rm,rs,4])
                    q.append([key[0],key[1],rm,rs,6])
                else:
                    q.append([key[0],key[1],rm,rs,1])
                    q.append([key[0],key[1],rm,rs,3])
                    q.append([key[0],key[1],rm,rs,5])
                    q.append([key[0],key[1],rm,rs,7])
        else: q.append([key[0],key[1],value[0][0],value[0][1],value[0][2]])
    return q
    
        
        
N,M,K = map(int,input().split())
dir = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
queue=[]
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    queue.append([r,c,m,s,d])
for _ in range(K):
    queue=bfs()
    # print(*queue)
result=0
for i in range(len(queue)):
    result+=queue[i][2]
print(result)
