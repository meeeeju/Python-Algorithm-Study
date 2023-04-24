#BaekJoon 2343 기타레슨
# 42340 KB / 300 ms
import sys
def check(length):
    sum= 0  # 강의 길이
    lec = 1  # 강의수
    for i in range(N):
        if sum+nlist[i]>length:  # length(블루레이 길이)보다 커지면 lec 증가해주고, sum 초기화
            lec+=1
            if lec > M : return False  # 만약, M개수보다 커지면 False 리턴
            sum=nlist[i]
            continue
        sum+=nlist[i]
    return True  # False를 리턴하지 않고 끝까지 돌았다는 것은 legnth(블루레이 길이)를 기준으로, M만큼 자를 수 있다는 것이므로 True 반환
        
def find(start,end):
    global min_length
    if start>end: return 
    mid = (start+end)//2
    if check(mid):  # 블루레이 길이(mid)로 M만큼 나눌 수 있을 때 mid_length 업데이트해줌
        min_length = min(min_length,mid)
        find(start,mid-1)
    else :
        find(mid+1,end)
    
N,M = map(int,sys.stdin.readline().split())
nlist = list(map(int,sys.stdin.readline().split()))
min_length = sum(nlist)  # 블루레이 값 (구해야하는 값)
find(max(nlist),sum(nlist))  # 최솟값 : 입력받은 값 중 가장 큰 강의 길이 , 최댓값 : 모든 강의의 합
print(min_length)

