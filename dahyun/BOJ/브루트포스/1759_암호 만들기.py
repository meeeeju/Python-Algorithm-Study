# 31256 KB / 56 ms
import sys
def dfs(password,vCount,index):
    if len(password)>L : return # 길이가 L 이상이면 리턴
    # 길이가 L이고, 최소 두 개의 자음 , 최소 한 개의 모음인지 확인 , 해당 값이 결과 리스트에 포함되어 있는지 확인
    if len(password)==L and L-vCount>=2 and vCount>=1 and not password in result:  
        result.append(password)
        return
    for i in range(index+1,C): # 현재 인덱스부터 끝까지 돌면서 dfs 돌기
        if alpha[i] in vowel : dfs(password+alpha[i],vCount+1,i)
        else: dfs(password+alpha[i],vCount,i)
    return
    
L,C = map(int,sys.stdin.readline().split())
alpha = list(map(str,sys.stdin.readline().split()))
alpha.sort()
vowel=['a','e','i','o','u']
result=[]

for i in range(C): # 시작지점 i
    if alpha[i] in vowel : dfs(alpha[i],1,i)
    else: dfs(alpha[i],0,i)

for r in result: print(r)
