# 31256 KB / 40 ms
import sys
input = sys.stdin.readline
def check(n):
    num=0
    visited[n]=True  # 해당 위치의 값 True
    # 가로
    temp1,temp2=n,n
    for i in range(5):
        if temp1 in right and temp2%5==1 and visited[temp1] and visited[temp2]: num+=1; break # temp1이 right 해당하고 temp2이 left 해당 시 한줄 완성이므로 num값 증
        if 0>=temp1 or temp1>=26 or 0>=temp2 or temp2>=26 or not visited[temp1] or  not visited[temp2] : break # 만약 가로줄 중 방문하지 않은 위치가 있다면 break
        if temp1%5!=0 and visited[temp1] : temp1+=1  # rigth , left 해당하지 않고 해당 위치 방문하면 temp1은 +1 (증가)
        if temp2%5!=1 and visited[temp2] : temp2-=1  # rigth , left 해당하지 않고 해당 위치 방문하면 temp1은 -1 (감소)
        
    # 세로
    temp1,temp2=n,n
    for i in range(5):
        if 20<temp1<26 and 0<temp2<6 and visited[temp1] and visited[temp2]: num+=1;break  # temp1이 마지막 줄에 위치하고, temp2가 첫번째 줄에 해당하면 num 증가
        if 0>=temp1 or temp1>=26 or 0>=temp2 or temp2>=26 or not visited[temp1] or not visited[temp2] : break # 만약 세로줄 중 방문하지 않은 위치가 있다면 break
        if temp1<20 and visited[temp1] : temp1+=5 # 마지막 줄이지 않을 때, temp1+5
        if temp2>=6 and visited[temp2] : temp2-=5 # 첫째 줄 이지 않을 때, temp2-5
    # 대각선
    if n in diagonal1 and visited[1] and visited[7] and visited[13] and visited[19] and visited[25]: num+=1
    if n in diagonal2 and visited[5] and visited[9] and visited[13] and visited[17] and visited[21] : num+=1
    
    return num
board=[0 for _ in range(26)]
visited=[False for _ in range(26)]
diagonal1 = [1,7,13,19,25]  # 대각선 1
diagonal2 = [5,9,13,17,21]  # 대각선 2
left = [1,6,11,16,21]  # 왼쪽 제한
right = [5,10,15,20,25]  # 오른쪽 제한
num=1  
for i in range(1,6):
    temp = list(map(int,input().split()))
    for j in range(5):
        board[temp[j]]=num
        num+=1
num=0  # 빙고 수
result=0  # 철수가 "빙고"를 외칠 때 , 사회자가 부른 숫자의 개수
nlist = [list(map(int,input().split())) for _ in range(5)]  # nlist : 사회자가 부르는 숫자
for i in range(5):
    for j in range(5):
        result+=1
        num+=check(board[nlist[i][j]])  # ex) nlist[i][j]=7 일때 board[nlist[i][j]] :  7의 위치
        if num>=3: print(result); exit();
print(result)
'''
숫자들은 총 1~25로 일차원 배열로 생각 !
board[n] : n의 위치 저장
visited[]로 해당 위치를 방문했는지 확인

ex) 
숫자 5는 board[5]에 몇 번째 숫자인지 저장
visited[5]는 5 위치를 방문했는지 확인
'''
