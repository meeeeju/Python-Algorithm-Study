#메모리 :31256 시간:56ms
computer=int(input())
connect=int(input())
array=[[] for i in range(computer+1)]
visit=[0]*(computer+1)

for i in range(connect):
    a,b=map(int,input().split())
    array[a]+=[b]
    array[b]+=[a]
   
def dfs(connect):
    visit[connect]=1
    for ab in array[connect]:
        if visit[ab]==0:
            dfs(ab)
           
dfs(1)
print(sum(visit)-1)
