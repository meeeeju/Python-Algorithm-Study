# 31256	40
import sys
input = sys.stdin.readline


'''
# 철수의 빙고판
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18

# 사회자
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15'''

board = [[] for _ in range(5)]
numbers = [[] for _ in range(5)]
visited =[False for _ in range(26)]

for i in range(5):  # 철수
    board[i]=list(map(int,input().split()))

for i in range(5):  # 사회자
    numbers[i]=list(map(int,input().split()))

bingo =[[],[]] # 현재 빙고 갯수
left_flag= True
right_flag = True

def isBingo(y,x):

    global left_flag
    global right_flag
    score = 0

    if not x in bingo[0]:
        for i in range(5):  # 세로 체크
            if  not visited[board[i][x]]:
                break
        else:
            bingo[0].append(x)
            score +=1

    if not y in bingo[1]:
        for i in range(5):  # 가로 체크
            if not visited[board[y][i]]:
                break
        else:
            bingo[1].append(y)
            score +=1

    if (x == y) and left_flag :
        for i in range(5):
            if not visited[board[i][i]]:
                break
        else:
            score +=1
            left_flag = False

    # 대각선 체크해줘야함 
    if (x+y ==  4 )  and right_flag:
        for i in range(5):
            if not visited[board[i][4-i]]:
                break
        else:
            score +=1
            right_flag = False  
    return score


def find_number(num):
    for k in range(5):
        for l in range(5):
            if board[k][l]==num:
                visited[num]= True
                return (k,l)
                

def main():
    all_score = 0
    cnt = 0
    for i in range(5):
        for j in range(5):
            y,x = find_number(numbers[i][j])
            all_score += isBingo(y,x)
            cnt +=1
            if all_score >= 3:
                return cnt
            
print(main())
