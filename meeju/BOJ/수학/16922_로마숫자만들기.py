# 31256	44
import sys
input = sys.stdin.readline

# 조합,순열 재귀함수로 구현 <백트래킹>

N = int(input())
rome = [1,5,10,50]
path = [0]*N
result_set = set()

def comb(depth, start):
    if depth == N :
        # print(path,end=',')
        result_set.add(sum(path))
        return
    for i in range(start,len(rome)):
        path[depth]= rome[i]
        comb(depth+1,i)
comb(0,0)

print(len(result_set))