# 58920 KB / 240 ms
import sys
N,X = map(int,sys.stdin.readline().split())  # N : 지난 일수 , X : 기간
nlist=list(map(int,sys.stdin.readline().split())) # N기간 동안 방문자 수
sum=0  # 전체 합
end=0  # 마지막 위치
result=0  # 최대 방문자 수
count=1   # 최대 방문자가 된 기간 수
for start in range(N):
    while end-start<X and end<N:  # 갈 수 있을 만큼 고고 (인덱스는 0부터 시작하므로 end-start가 X-1일 때 사실 상 맞음)
        sum+=nlist[end]
        end+=1
    if end-start==X:   # 만약 , end-start가 X면 값 업데이트 (end 값이 end-start가 X-1 일때도 while 문에 들어가므로 end값이 하나 더 증가하게 됨)
        if result==sum : count+=1  # 최종값과 sum 값이 같다면 기간 개수인 count 증가
        elif result<sum :   # 만약 방금 구한 sum 값이 가장 많은 방문자 수라면 result 초기화해주고 , 기간 개수인 count도 1로 초기화
            result=sum
            count=1
    sum-=nlist[start]  # 
if result==0 : print("SAD")
else:
    print(result)
    print(count)
