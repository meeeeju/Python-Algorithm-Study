# 31256kb /	40ms
# 블로그 참고해서  새로 짬 !
import sys
input = sys.stdin.readline

# 1 검은색, 2 흰색, 0 놓이지 않은 자리 

board = [ 0 for _ in range(19)]
for i in range(19):
    board[i] = list(map(int,input().split()))

dx= [0,1,1,-1]
dy = [1,1,0,1]

def main():
    for y in range(19):     # x,y 바꿔줘도 정답 가능
        for x in range(19):
            main = board[x][y]
            if main== 0:  # 아무것도 없으면 pass
                continue
            for i in range(4):
                cnt =1      # board[x][y] 자리의 바둑돌 색깔
                nx = x 
                ny = y

                for j in range(4):
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or nx >= 19 or ny <0 or ny >= 19: # 바둑판의 크기를 초과하면 
                        break
                    if board[nx][ny] != main:      # 바둑돌의 색깔이 메인과 다르면
                        break
                    cnt += 1 

                if cnt == 5:
                    # 육목 체크
                    if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == main:
                        continue
                    if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == main:
                        continue
                    return main,x,y
                        
    return 0 ,0,0

color, x,y = main()

if color :
    print(color)
    print(x+1,y+1)
else:
    print(0)
