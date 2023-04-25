#BaekJoon 2110 공유기 설치
# 38984 KB / 320 ms
# 블로그 참고 - 공유기 설치할 수 있는 개수가 C보다 커지면 안된다고만 생각하고 계속 코드 짜고 있었음 ㅠ
import sys
def check(length): 
    start_wifi = 0  # 공유기 설치 위치
    wifi=1  # 공유기 설치 개수
    for i in range(1,N):
        if nlist[i]-nlist[start_wifi]>=length:  # 위치 차이(nlist[i]에서 공유기 설치 시작 위치 차이)가 length(내가 찾은 공유기 사이 거리)보다 크다
            start_wifi=i  # 공유기 설치 위치를 i번째로 초기화 (새로운 시작 !)
            wifi+=1  # 공유기 설치 개수 증가
            if wifi>=C : return True  # 만약 공유기 설치 개수가 C보다 같거나 커진다면 공유기 사이 거리를 더 늘릴 수 있다 -> 즉, 이 length로 공유기 잘 설치할 수 있음 (True)
    return False  # 공유기 설치를 모두 다 하지 못함 (False)

def find(start,end):  # 공유기 사이의 거리를 찾자 !!
    global max_length
    if start>end : return
    mid = (start+end)//2  
    if check(mid):  # 해당 mid 값으로 공유기 설치 잘 할 수 있다는 뜻이므로 max_length 업데이트
        max_length=max(max_length,mid)
        find(mid+1,end)  # 더 넓은 범위에 공유기 설치
    else:
        find(start,mid-1)  
        
input = sys.stdin.readline
N,C = map(int,input().split())   # N : 집 개수 , C : 공유기 개수
nlist = [int(input()) for _ in range(N)]   # nlist : 집의 좌표
nlist.sort()  # 위치 정렬
max_length=0
find(1,nlist[-1]-nlist[0])  # 최솟값 : 최소거리 , 최댓값 : 최대거리
print(max_length)
