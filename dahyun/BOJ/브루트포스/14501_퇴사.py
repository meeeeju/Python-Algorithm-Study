#알고리즘 분류 확인함
# 31256 KB / 44 ms
import sys
N=int(sys.stdin.readline())
t_list,p_list=[],[]
dp=[0 for _ in range(N)]
for i in range(N):
    t,p=map(int,sys.stdin.readline().split())
    t_list.append(t)
    p_list.append(p)
for i in range(N):
    if i+t_list[i]>N: continue # 해당 고객의 상담에 필요한 시간이 N을 넘음
    dp[i]=p_list[i]
for i in range(N):
    for j in range(i+t_list[i],N): # i 에서 끝난 이후를 모두 돌음 (j)
        if dp[j]==0: continue  # 이때 dp[] 값이 0이라는 것은 해당 고객의 상담에 필요한 시간이 N을 넘기 때문이므로 continue!
        if i<j:  dp[j]=max(dp[j],dp[i]+p_list[j]) # i와 j가 같은 경우도 있으므로 조건문 걸어준다. 자기 자신과 i와 해당 날짜의 값 더한 값 비교
print(max(dp))

