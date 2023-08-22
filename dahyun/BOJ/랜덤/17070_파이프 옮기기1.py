# 블로그 참고 - dp...
# https://velog.io/@eunseokim/BOJ-17070번-파이프-옮기기-1-dp-풀이-python
'''
0 → ─(가로), 1 → /(대각선), 2 → |(세로)

[현재 가로 파이프의 끝 개수] = [왼쪽 칸의 가로 파이프 끝 개수] + [왼쪽 칸의 대각선 파이프 끝 개수]
[현재 칸의 세로 파이프의 끝 개수] = [위쪽 칸의 세로 파이프 끝 개수] + [위쪽 칸의 대각선 파이프 끝 개수]
[현재 칸의 대각선 파이프의 끝 개수] = [(왼쪽 위 대각선)칸의 가로 파이프 끝 개수] + [(왼쪽 위 대각선)칸의 세로 파이프 끝 개수] + [(왼쪽 위 대각선)칸의 대각선 파이프 끝 개수)]

dp는 가로, 세로, 대각선 칸을 구현하기 위해 3차원 배열을 사용

   dp[0][row][col] = 가로 파이프에 대한 dp
   dp[1][row][col] = 대각선 파이프에 대한 dp
   dp[2][row][col] = 세로 파이프에 대한 dp
   
'''

def solution():

    # 1행 미리 처리하기 → (3) 과정 : 첫째 행은 가로만 올 수 있다.
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
	
    
    # 1행과 1열을 제외 : 첫번째 행은 항상 가로 파이프만 존재 / 첫번째 열은 시작이 가로 파이프이기때문에 신경 쓸 필요 x
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
                
	    # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1] # 가로 + 대각선
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c] # 세로 + 대각선
    
    
    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()
