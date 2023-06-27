# 120816 KB / 568 ms (pypy)
# 36548 KB / 3412 ms (python)
import sys
input = sys.stdin.readline
def check(a,b):
    global result
    for i in range(5):
        total1,total2,total3,total4=nlist[a][b],nlist[a][b],nlist[a][b],nlist[a][b]
        total3_1,total3_2,total3_3,total3_4 = nlist[a][b],nlist[a][b],nlist[a][b],nlist[a][b] 
        for j in range(3):
            a1,b1 = polyomino[i][j][0],polyomino[i][j][1]
            #1 그대로 
            ta=a+a1
            tb=b+b1
            if 0<=ta<N and 0<=tb<M:
                total1+=nlist[ta][tb]
            else: total1=-100
            if i==2 or i==3:  # 3, 4 번째 모양은 반전시킬 수 있음
                tb1=b+(b1*-1)  # y를 반대로 |- -> -| 
                if 0<=ta<N and 0<=tb1<M:
                    total3_1+=nlist[ta][tb1]
                else: total3_1 = -100
            #2 *-1
            ta=a+(a1*-1)
            tb=b+(b1*-1)
            if 0<=ta<N and 0<=tb<M:
                total2+=nlist[ta][tb]
            else: total2=-100
            if i==2 or i==3:
                tb1=b+b1
                if 0<=ta<N and 0<=tb1<M: # 해당 위치가 범위 안에 포함하는지 확인
                    total3_2+=nlist[ta][tb1]
                else: total3_2 = -100 # 포함되지 않는다면, 더이상 볼 필요 없으므로 -100으로 초기화
            #3 대칭 (x 반대로)
            ta=a+(b1*-1)
            tb=b+a1
            if 0<=ta<N and 0<=tb<M:
                total3+=nlist[ta][tb]
            else:
                total3=-100
            if i==2 or i==3:
                tb1=b+(a1*-1)
                if 0<=ta<N and 0<=tb1<M:
                    total3_3+=nlist[ta][tb1]
                else: total3_3 = -100
            #4 대칭 (y 반대로)
            ta=a+b1
            tb=b+(a1*-1)
            if 0<=ta<N and 0<=tb<M:
                total4+=nlist[ta][tb]
            else: total4=-100
            if i==2 or i==3:
                tb1=b+a1
                if 0<=ta<N and 0<=tb1<M:
                    total3_4+=nlist[ta][tb1]
                else: total3_4 = -100
        if i==2 or i==3: result=max(result,total1,total2,total3,total4,total3_1,total3_2,total3_3,total3_4) # 2,3번째 모양은 반전시킨 것까지 모두 확인
        else:  result=max(result,total1,total2,total3,total4) # 0,1,4 모양은 반전 딱히 안봐도 됨 
                
            
N,M = map(int,input().split())
nlist = [list(map(int,input().split())) for _ in range(N)]
polyomino=[[(0,1),(0,2),(0,3)],[(0,1),(1,1),(1,0)],[(1,0),(2,0),(2,1)],[(1,0),(1,1),(2,1)],[(0,1),(0,2),(1,1)]] # 좌표로 설정해둠
result=0
for i in range(N):  # 모든 좌표를 돌면서 확인함
    for j in range(M):
        check(i,j)
print(result)
