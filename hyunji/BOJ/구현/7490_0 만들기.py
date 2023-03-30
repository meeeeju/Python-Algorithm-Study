#블로그 참고
import sys
import copy
input=sys.stdin.readline

def backtracking(v):#아스키 코드 순서대로 백트래킹
    if len(v)==N-1:
        arr.append(copy.deepcopy(v))
        return
    #아스키 코드 34
    v.append(' ')
    backtracking(v)
    v.pop()

    #아스키 코드 44
    v.append('+')
    backtracking(v)
    v.pop()

    #아스키 코드 45
    v.append('-')
    backtracking(v)
    v.pop()

T=int(input())
for _ in range(T):
    N=int(input())
    arr=[]
    backtracking([])
    
    for i in arr:
        temp=""
        for j in range(1,N):
            temp+=str(j)+str(i[j-1])
        temp+=str(N)

        if eval(temp.replace(' ',''))==0:
            print(temp)
print()
