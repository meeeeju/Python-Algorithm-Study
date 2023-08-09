import sys
import math
input = sys.stdin.readline


# # 이것도 얕은 복사 아닌가?????
# copy_place = [[place[i][j] for j in range(N+1)] for i in range(N+1)]
# copy_place[1][0]=[1,0,0]
# print(copy_place[1][0])
# print(place[1][0])

'''
4 2 1   # N, M, K
1 1 5 2 2 
1 4 7 1 6'''


def move(): # 움직이기

    

    for i in range(N+1):
        for j in range(N+1):
            while place[i][j]:
                fireball = place[i][j].pop()
                ni,nj = i,j
                if fireball[2] == 7 or fireball[2] == 0 or fireball[2] == 1 :
                    ni = i - si
                    if ni <= 0:
                        ni +=N
                if fireball[2] == 5 or fireball[2] == 4 or fireball[2] ==3 :
                    ni = i + si
                    if ni > N:
                        ni -=N
                if fireball[2] == 7 or fireball[2] == 6 or fireball[2] == 5 :
                    nj= j - si
                    if nj <= 0:
                        nj +=N
                if fireball[2] == 1 or fireball[2] == 2 or fireball[2] == 3 :
                    nj= j + si
                    if nj > N:
                        nj -=N
                place[ni][nj].append(fireball)
            
# fireball 질량, 속도, 방향
def divideFireball():
    for i in range(N+1):
        for j in range(N+1):
            if len(place[i][j]) >=2 :

                sum_m = 0
                sum_s = 0
                dir = (place[i][j][0][2]) % 2 # 첫번째 파이어볼의 방향
                flag = True # 모두 다 짝수거나 홀수거나 

                for fireball in place[i][j]:
                    sum_m += fireball[0]
                    sum_s += fireball[1]
                    if (fireball[2] % 2) != dir :
                        flag = False
                new_m = math.floor(sum_m /5)
                new_s = math.floor(sum_s/len(place[i][j]))

                place[i][j] = []    # 공간 초기화해주기

                if not new_m :  # 질량이 0이면 파이어볼 소멸
                    continue    

                for i in range(4):
                    if flag :   # 모두 짝수거나 홀수이면 (0, 2, 4, 6)
                        place[i][j].append([new_m,new_s,i*2])
                    else:
                        place[i][j].append([new_m,new_s,i*2+1])

# 초기화
N, M, K = map(int,input().split())  # N : 격자 , M : 파이어볼의 갯수 , K : 명령 횟수
place = [[[] for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(M):  
    ri, ci, mi, si, di= map(int,input().split())    # 위치(행,열), 질량, 속도, 방향
    place[ri][ci].append([mi,si,di])




# 명령 수행
for _ in range(K):

    move()
    divideFireball()



# result = 0 
# # 남아있는 총 질량 구하기
# for i in range(N+1):
#     for j in range(N+1):
#         while place[i][j]:
#             result += place[i][j].pop()[0]
# print(result)


                        

