# 31256kb /	40ms
import sys
input = sys.stdin.readline

'''3 90 10
100 90 80'''

def main():
    for i in range(N):  # 1부터 N 까지 돌림
        if ranking[i] <= score:
            spot = i
            if N < P:     # 랭킹에 더 추가될 수 있는 경우
                return spot+1
            else:           # 랭킹이 꽉 찬 경우
                for j in range(spot,N):
                    if ranking[j] < score:
                        return spot
                else:
                    return -1     
    if N < P :
        return N+1              
    return -1


N,score, P = map(int,input().split()) # 현재 랭킹에 있는 점수의 갯수, 태수의 점수, 리스트에 올라갈 수 있는 점수의 갯수
if N==0 and P > 0:
    print(1)
else:
    ranking =list(map(int,input().split()))
    print(main())


