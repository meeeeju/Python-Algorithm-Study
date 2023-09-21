# 31256	44 
import sys
input = sys.stdin.readline


'''
7
3
1
1
5
5
4
6'''

N = int(input())


listA = [i for i in range(1,N+1)]   # 첫째
listB = [0 for _ in range(N)]

result_set = set()
dict_table={}


for i in range(N):
    s =int(input())
    listB[i]= s
    dict_table[i+1] = s # listA 와 listB 간의 관계 
    
def recur(v,s):        
    visited[v-1] = 1
    w = dict_table[v]
    # if w == v : # 방문한 곳을 다시 방문
    #     return True
    if visited[w-1] == 1 and w == s: # 방문된 곳이면
        return True
    elif visited[w-1] == 1:
        return False
    else:
        return recur(w,s) 
    
        

visited = [0 for _ in range(N)]
for i in range(0,N):
    visited = [0 for _ in range(N)] # 처음에는 방문 0 으로 초기화 -> 
    if (i+1) not in result_set:
        if recur(i+1,i+1) : 
            for i in range(N):
                if visited[i] == 1:
                    result_set.add(i+1)
result = sorted(list(result_set))
print(len(result),*result)



