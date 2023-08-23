# 31256	932
import sys
input = sys.stdin.readline

# 백트래킹으로 풀고싶다 


N, M = map(int,input().split()) # N : 아이스크림 종류의 수 ,  M : 섞어먹으면 안 되는 조합의 수 

bad_combi ={}
visited = [False] * (N+1)
for i in range(1,N+1):
    bad_combi[i]=[]


for i in range(M):
    a,b = map(int,input().split())
    bad_combi[a].append(b)
    bad_combi[b].append(a)
 
def find(start):
    global cnt

    if len(combi) == 3:
        cnt +=1
        # print(combi)
        return 
    for i in range(start,N+1):  # start 부터 M 내에서 선택가능하므로

        flag = True
        if not visited[i]:

            for c in combi:
                if i  in bad_combi[c]:  # 피해야되는 아이스크림인지 검사하기
                    flag = False
                    break
            if not flag: 
                continue
            visited[i] = True
            combi.append(i)
            find(i+1)
            visited[i] = False
            combi.pop()


combi = []
cnt = 0
find(1)

print(cnt)
