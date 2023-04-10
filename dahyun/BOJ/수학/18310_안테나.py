#BaekJoon 18310 안테나
# 53144 KB / 152 ms
# 질문 게시판 참고
N=int(input())
nlist =list(map(int,input().split()))
if N==1: 
    print(nlist[0])
else: 
    nlist.sort()  # 정렬
    left=1  # 왼쪽 집 개수
    right=N-1  # 오른쪽 집 개수
    for i in range(0,N):
        if left>=right :  # 왼쪽 집 개수가 더 많아질 때
            print(nlist[i])
            break
        left+=1  # 왼쪽 집 개수 증가
        right-=1  # 오른쪽 집 개수 감소
