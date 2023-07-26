# 완전 탐색 실패 ,,
# https://www.acmicpc.net/board/view/58247 (반례 한개 안 맞음)
import sys
input = sys.stdin.readline

'''
3
CCP
CCP
PPC'''

N = int(input())

candy_game = [[]for _ in range(N)]

for i in range(N):
    candy_game[i]= list(input().rstrip())

result = 0

def check_row(si,sj):

    global result 
    if result > N - sj :
        return result
    
    cnt = 1
    main_candy = candy_game[si][sj]
    temp = [k for k in candy_game[si]] # 행

    flag = False

    for x in range(sj+1,N):
        if temp[x] == main_candy:
            cnt +=1
        
        else:
            if not flag:
                flag = True
                if si > 0:
                    if main_candy == candy_game[si-1][x]:
                        temp[x]= candy_game[si-1][x]
                        cnt +=1
                        continue
                if si < N-1 :
                    if main_candy == candy_game[si+1][x]:
                        temp[x]= candy_game[si+1][x]
                        cnt +=1 
                        continue
                if x < N -1 :
                    if main_candy == temp[x+1]:
                        temp[x],temp[x+1] = temp[x+1],temp[x]
                        cnt +=1
                        break
            else:
                break
    return cnt


def check_column(si,sj):
    cnt = 1
    main_candy = candy_game[si][sj]
    temp = [candy_game[k][sj] for k in range(N)] # 행


    flag = False
    for x in range(si+1,N):
        if temp[x] == main_candy:
            cnt +=1
        else:
            if not flag:
                flag = True
                if sj > 0:
                    if main_candy == candy_game[x][sj-1]:
                        temp[x]= candy_game[x][sj-1]
                        cnt +=1
                        continue
                if sj < N-1 :
                    if main_candy == candy_game[x][sj+1]:
                        temp[x]= candy_game[x][sj+1]
                        cnt +=1 
                        continue
                if x < N -1 :
                    if main_candy == temp[x+1]:
                        temp[x],temp[x+1] = temp[x+1],temp[x]
                        cnt +=1
                        break
            else:
                break
    return cnt


def main():
    global result
    for i in  range(N):
        for j in range(N):
            result_row = check_row(i,j)
            result_column = check_column(i,j)
            result = max(result_row,result_column,result)
            if result == N :
                return 

    return 

main()
print(result)