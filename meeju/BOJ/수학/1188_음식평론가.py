# 블로그 참고 / 질문 게시판 참 :  https://zzang9ha.tistory.com/231 
import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # N : 소세지 수, M : 음식평론가 수


def GCD(a,b):
    r = 1 # 임의의 수 넣어두기
    while(r):
        r = a % b
        a = b
        b = r
    return a

print(M-GCD(N,M))


# print( M - GCD(N,M))

# while( M <= N):
#     N -= M

# if N == 0 :
#     print(0)
# elif (M % N == 0 ):
#     print((M//N -1)* N )
# else:
#     print( (M//N)*N)






