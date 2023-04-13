# 42176kb /	124ms
# 블로그 풀이로직 참고
# 왜 수빈이 기점으로 한번만 해주면 되는지 이해가 잘 안됨
import sys
input = sys.stdin.readline

'''3 3
1 7 11'''

def GCD(x,y):   # x,y 크기 상관없음
    while (y):
        x,y = y,x%y
    return x

N, S = map(int,input().split()) # N : 동생의 수, S : 수빈이의 위치

A_list = list(map(int,input().split())) # 동생들의 위치
A_list.sort()
cnt = 0
maximum_dis = 0

dis_to = [abs(S-A_list[i]) for i in range(N)]   # 수빈이와 동생들간의 거리 차

maximum_dis = dis_to[0]
for i in range(N):
    maximum_dis=GCD(maximum_dis,dis_to[i])

    
print(maximum_dis)

        






