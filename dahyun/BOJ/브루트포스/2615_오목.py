# 31256 KB / 40 ms
import sys
def find_winner(nx,ny,player):
    for x,y in direction:
        if baduk[nx][ny]==player: count=1
        else: count=0
        pro=1
        finish_go,finish_back=False,False # 커지는 값. 작아지는 값의 종료 여부 
        while True:
            if 0<=nx+(x*pro)<19 and 0<=ny+(y*pro)<19:  # 다음 위치가 범위에서 벗어나는지 확인 (커지는 값)
                if not finish_go and baduk[nx+(x*pro)][ny+(y*pro)]==player: count+=1 # 종료하지 않고, 다음위치 값이 player이라면 count 증가
                else : finish_go=True  # 다음 값이 player과 같지 않다면 종료
            else : finish_go=True  # 다음 값이 범위 초과시 종료
            
            if 0<=nx-(x*pro)<19 and 0<=ny-(y*pro)<19:  # 다음 위치가 범위에서 벗어나는지 확인  (작아지는 값)
                if not finish_back and baduk[nx-(x*pro)][ny-(y*pro)]==player: count+=1 # 종료하지 않고, 다음위치 값이 player이라면 count 증가
                else : finish_back=True
            else : finish_back=True
            
            if finish_go and finish_back : break  # 둘 다 종료 시 종료
            pro+=1
        if count==5: return True  # count가 5개라면 리턴
                
    return False
                
        
    
baduk=[]  # 19x19 바둑판
for i in range(19):
    baduk.append(list(map(int,sys.stdin.readline().split())))
    
direction=[(1,0),(0,1),(1,-1),(1,1)] # 오른쪽 , 아래 , 왼쪽 아래, 오른쪽 아래

for j in range(19): # 세로
    for i in range(19): # 가로
        if baduk[i][j]==1 and find_winner(i,j,1) :
            print(1)
            print(i+1,j+1)
            exit()
        elif baduk[i][j]==2 and find_winner(i,j,2):
            print(2)
            print(i+1,j+1)
            exit()
print(0)
            
