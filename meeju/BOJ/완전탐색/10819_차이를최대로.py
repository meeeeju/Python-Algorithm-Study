# 	35692	140
import sys
from itertools import product
from itertools import permutations
input = sys.stdin.readline

'''
6 
20 1 15 8 4 10'''

N = int(input()) # 3<= N <=8
arr = list(map(int,input().split()))
res = 0

combi_list = list(permutations(arr,N))
for combi in combi_list:
    temp = 0
    for i in range(N-1):
        temp += abs(combi[i]-combi[i+1])
    if temp > res :
        res = temp
print(res)



'''
# 백트래킹 - 블로그 참조
n = int(input())
lst = list(map(int, input().split()))
#인덱스 방문 처리
visited = [False for _ in range(n)]
ans = 0
tem = [0 for _ in range(n)]

# 배열의 순서를 바꿈, 중복 불가 순열
def recur(cur):
    global tem
    global ans

    if cur == len(lst):
        ans_tem = 0
        for i in range(n-1):
            ans_tem += abs(tem[i]-tem[i+1])
        ans = max(ans, ans_tem)
        return
        
    # 인덱스의 순열
    for i in range(n):
        if visited[i]:
            continue
        tem[cur] = lst[i]
        visited[i] = True
        recur(cur + 1) # 다음 값 담기
        visited[i] = False

recur(0)
print(ans)'''