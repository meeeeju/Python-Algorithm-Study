#BaekJoon 19942 다이어트
# 32276 KB / 80 ms
import sys
input = sys.stdin.readline
def dfs(nutrients,total,price):  # nutrients : 선택한 재료들 , total : 영양분의 합 , price : 가격
    tp,tf,ts,tv = total
    for i in range(len(hap)):
        if total[i]<hap[i]: break  # 최소 비용들보다 더 작다면, 다른 재료 더 선택해야함 
    else: result.append((price,nutrients)); return  # result에 추가
    if nutrients : start = nutrients[-1]  # 만약 nutrients에 값이 존재하면 start는 마지막 값
    else: start=0  # 처음 불렸을 떄, start는 0
    for i in range(start+1,N+1):
        if not i in nutrients:  # i 가 nutrients에 포함되지 않는다면,
            # mp, mf, ms, mv = nlist[i]
            dfs(nutrients[:]+[i],[tp+nlist[i-1][0],tf+nlist[i-1][1],ts+nlist[i-1][2],tv+nlist[i-1][3]],price+nlist[i-1][4])
    return 
            
 
result=[]
N=int(input())
hap=list(map(int,input().split()))   # 필요한 최소 영양소 값
nlist=[list(map(int,input().split())) for _ in range(N)]
dfs([],[0,0,0,0],0) 
result.sort()  # result 정렬
if result: 
    print(result[0][0])
    print(*result[0][1])
else: print(-1)
