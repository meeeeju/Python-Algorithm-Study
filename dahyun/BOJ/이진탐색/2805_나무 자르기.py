#BaekJoon 2805 나무 자르기
# 143400 KB / 1652 ms
import sys
def check(length):  # length 만큼 잘랐을 때 괜찮은지 확인하는 함수
    sum=0
    for i in range(N):
        if nlist[i]>length:  # 만약 잘라갈 수 있는 나무면, sum에 잘라진 크기만큼 더함
            sum+=(nlist[i]-length)
            if sum>=M : return True  # 만약 들고가야하는 나무크기(M)만큼 구했다면 True 리턴
    if sum<M : return False  # 끝까지 돌았다면 들고가야하는 나무크기(M)만큼 구하지 못했다는 것이므로 False 리턴
def find(start,end):
    global max_length
    if start>end: return
    mid = (start+end)//2
    if check(mid):  # True면 max값으로 업데이트 후, 더 큰 나무크기를 구할 수 있는지 확인
        max_length=max(max_length,mid)
        find(mid+1,end)
    else:  # Flase면 잘라갈 수 있는 나무 크기가 더 작다는 것이므로, 더 작은 나무크기를 구할 수 있게 범위 지정
        find(start,mid-1)
        
    
N,M = map(int,sys.stdin.readline().split())
nlist = list(map(int,sys.stdin.readline().split()))
max_length=0
find(0,max(nlist)-1) # 최솟값 : 모든 나무를 다 잘라갈 수도 있으므로 0 , 최댓값 : 모든 나무를 다 잘라가지 않을수 있으므로 max(nlist),, 근데 M의 최솟값이 1이네..? -> max(nlist)-1로 바꿔줌
print(max_length)
