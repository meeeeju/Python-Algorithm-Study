# 	42340kb / 224ms
# 블로그 조금 참고 ^^

import sys
input  = sys.stdin.readline

'''
9 3  강의 수, 블루레이 갯수
1 2 3 4 5 6 7 8 9  강의의 길이 
'''

N,M =map(int,input().split())   # N : 강의 수, M : 블루레이 갯수
class_info = list(map(int,input().split()))
start = max(class_info)
end = sum(class_info)

def find_length():
    
    global start,end

    bluelay_cnt =1
    while (start <= end):
        mid = (start+end)//2    # 블루레이 용량

        temp = 0
        bluelay_cnt = 1
        for i in class_info:
            if temp + i > mid :
                temp = i
                bluelay_cnt +=1
            else:
                temp +=i
        if bluelay_cnt <= M :
            # if bluelay_cnt == M : # 이 조건 빼야됨 !
            #     return mid
            end = mid -1
        elif bluelay_cnt > M :
            start = mid +1
    return start
        
print(find_length())


'''
어떻게 이진탐색을 시킬지가 관건이였던 문제,,,!
우선 인덱스랑 값 중에 뭘로 탐색을 시킬 것인지도 생각해보아야함
이 문제는 값으로 이진탐색을 해야되는 문제이다. 
mid를 무엇으로 해야할지 고민이 많았는데 앞으로 정답을 기준으로 잡으면 될듯(야메긴해)

1. 블루레이의 크기를 기준 값으로 잡는다.
2. 값을 기준으로 그룹을 나누어본다.
3. 나온 그룹의 갯수가 문제에서 요구하는 조건 보다 큰 경우 start = mid+1
4. 작거나 같은 경우 end = mid -1
5. start 반환'''
