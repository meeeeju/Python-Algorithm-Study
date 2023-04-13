#BaekJoon 17497 계산기
# 블로그참고
# 31256 KB / 44 ms
'''
def cal():
    queue=[(2,['+'])] # 전체값 , 부호값
    visited=[False for _ in range(10*N)]
    visited[2]=True
    while queue:
        tot , clist = queue.pop(0)
        visited[tot]=True
        if len(clist)>100  or tot>(2**63) : return -1
        
        # if (clist[-1]==0 and i==2) or (clist[-1]==1 and i== 3) or (clist[-1]==2 and i==0) or (clist[-1]==3 and i==1): continue 
        
        if tot>N:   # 전체가 N을 넘어갔을 때는 빼기 , 나누기만
            new_m = (tot-2)
            new_d = (tot//2)
            if new_m==N : return clist+['-']
            elif new_d==N : return clist+['/']
            if not visited[new_m] and clist[-1]!='*':
                queue.append((new_m,clist+['-']))
            if not visited[new_d]:
                queue.append((new_d,clist+['/']))
        if tot<N :
            new_plus = tot+2
            new_pro = tot*2
            if new_plus==N : return clist+['+']
            elif new_pro==N : return clist+['*']
            if not visited[new_plus] and clist[-1]!='/':
                queue.append((new_plus,clist+['+']))
            if not visited[new_pro]:
                queue.append((new_pro,clist+['*']))
    #         if new==N : return clist+[calculate[i]]
    #         else : queue.append((new,clist+[calculate[i]]))
    #     elif tot<N and not (i==2 or i==3) :  # 전체가 N을 넘어가지 않을 때는 더하기, 곱하기만
    #         if new ==N : return clist+[calculate[i]]
    #         else : queue.append((new,clist+[calculate[i]]))
    return -1

# 2
def cal():
    tot =2
    clist = ['+']   
    for i in range(99):
        # if (clist[-1]==0 and i==2) or (clist[-1]==1 and i== 3) or (clist[-1]==2 and i==0) or (clist[-1]==3 and i==1): continue 
        if tot>(2**63)-1 or len(clist)>100: return -1
        if tot==N : return clist
        if tot>N:   # 전체가 N을 넘어갔을 때는 빼기 , 나누기만
            new_m = (tot-2)
            new_d = (tot//2)
            if new_m==N : return clist+['-']
            elif new_d==N : return clist+['/']
            if clist[-1]!='*': 
                tot = new_d
                clist.append("/")
            else :
                tot=new_m
                clist.append("-")
        if tot<N :
            new_plus = tot+2
            new_pro = tot*2
            if new_plus==N : return clist+['+']
            elif new_pro==N : return clist+['*']
            if clist[-1]!='/':
                tot= new_pro
                clist.append("*")
            else:
                tot= new_plus
                clist.append("+")
  '''      
# calculate = ['+','*','-','//'] # 0 : 더하기 , 1 : 곱하기 , 2: 빼기 , 3 : 나누기
# N=int(input())
# clist=cal()

# print(len(clist))
# print(*clist)

# 블로그
N=int(input())
nlist=[]
while N:
    if N&1 : nlist.append("[/]");N*=2
    elif N&2 : nlist.append("[+]"); N-=2
    else : nlist.append("[*]");N//=2
if len(nlist)>99 : print(-1)
else:
    print(len(nlist))
    print(' '.join(nlist[::-1]))
