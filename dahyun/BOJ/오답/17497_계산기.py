# 블로그 참고
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

'''
N->0으로 2진수를 통해 계산

만약 1이 남는다면, 0이 되지 못하니까 *2를 해줌
만약 2가 남는다면, 바로 -2
'''
