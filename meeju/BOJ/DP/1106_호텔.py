import sys
input = sys.stdin.readline
'''
12 2
3 5
1 1'''
C, N = map(int,input().split()) # C: 늘려야하는 고객의 수 , N: 도시의 개수


w=[]

max_people = 0
for i in range(N):
    cost, people = map(int,input().split())
    w.append((people,cost))
    max_people = max(max_people,people)
w.sort(key=lambda x:x[0])


last_c= C
C = max_people + C
dp=[float('inf') for _ in range(C+1)]
dp[0]=0
for p,c in w:
    dp[p]=min(dp[p],c)


for i in range(1,C+1): # dp[i] 

    for p,c in w:
        if i-p>0: # i=p
            dp[i]= min(dp[i],dp[i-p]+ c)
    
result = min(dp[last_c:C+1])
print(result)

