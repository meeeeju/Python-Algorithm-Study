#BackJoon 2512 예산
# 32276KB / 48 ms
import sys
sys.setrecursionlimit(int(1e5))

def sum(num): # num의 값을 포함하여 합계 구하기
    sum=0
    for n in nlist:
        if n<num : sum+=n
        else : sum+=num
    return sum

# 이분탐색을 구현하기 위한 재귀함수
def search(a,b): 
    if a==b : return  # a와 b가 같다면 무한 재귀를 돌으므로 바로 return
    mid = (b+a)//2  # 중간 값
    s=sum(mid) 
    if s<=total : total_list.append((mid,total-s)) # total보다 작거나 같다면 total_list에 중간값과 total과 얼만큼 차이나는지 저장
    if s>total : search(a,mid) # total보다 s가 크다면 s~mid 까지 탐색
    elif s<total : search(mid+1,b) # mid+1 ~ b 까지 탐색

   
N=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))
total=int(sys.stdin.readline())
total_list=[]  # 모든 가능한 값 저장하는 리스트
search(1,max(nlist)+1)  # 재귀함수 실행
print(sorted(total_list,key= lambda x: (x[1],x[0]))[0][0]) # (1)total과 차이값 (2)중간값 순으로 정렬 후 첫 번째 값 프린트
