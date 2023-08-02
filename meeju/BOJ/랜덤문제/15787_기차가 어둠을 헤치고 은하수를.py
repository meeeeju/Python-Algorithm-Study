# 비트마스크 사용 방법 찾아보았음

import sys
input = sys.stdin.readline

'''
5 5
1 1 1
1 1 2
1 2 2
1 2 3
3 1'''

N , M = map(int,input().split()) # N : 기차의 수 , M : 명령의 수 


train_list = [0 for _ in range(N+1)]    # 1부터 N번째 기차를 담기 위한 공간

for _ in range(M):
    order = tuple(map(int,input().split()))
    
    i = order[1]    # i : 기차 번호

    if order[0] == 1:   
        train_list[i] |= (1<<(20-order[2]))

    if order[0] == 2:   
        train_list[i] &= ~(1<<(20-order[2]))

    if order[0] == 3:   # 한 칸씩 뒤로 가기(오른쪽으로)
        train_list[i] = (train_list[i] >> 1) & 0b11111111111111111111
    
    if order[0] == 4:   # 한 칸씩 앞으로 가기 (왼쪽으로)
        train_list[i] = (train_list[i] << 1) & 0b11111111111111111111

# print(train_list)
print(len(set(train_list)))

