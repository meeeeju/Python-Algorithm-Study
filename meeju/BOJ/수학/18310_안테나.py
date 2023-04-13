# 53788kb /	276ms
import sys
input = sys.stdin.readline

'''4
5 1 7 9'''

N = int(input())    # 4 
location_list = list(map(int,input().split()))   # 5 1 7 9
location_list.sort()    # 1 5 7 9

start = 0 
end = N-1
min_cost = float('inf')
min_locate = 0

while (start <= end):   # 종료조건 주의 

    # 초기화 
    mid = (start + end) //2  # 버림 사용
    cost = 0 
    left = 0
    right = 0

    # 안테나간의 거리 구하기
    for i in range(N):
        if i < mid :
            left +=1
        elif i > mid:
            right +=1
        cost += abs(location_list[mid]-location_list[i])
    if left > right : # 왼쪽에 집이 더 많이 분포한 경우
        end = mid-1
    elif left < right : # 오른쪽에 집이 더 많이 분포한 경우
        start = mid +1
    if cost < min_cost:
        min_cost = cost
        min_locate = mid    # 주의 : 인덱스를 저장하고 있음  집의 위치 : location_list[min_locate]
    else:
        break

print(location_list[min_locate])




    



