# 31256	44
# 질문게시판 참고
import sys
input = sys.stdin.readline


N, K = map(int,input().split()) #  N : 공의 수, K : 팀원 수 

balls = (K*(K+1))//2

if balls < N :
    print(-1)
else:
    
    spare = N - balls
    if spare % K == 0:
        print(K-1)
    else:
        print(K)

