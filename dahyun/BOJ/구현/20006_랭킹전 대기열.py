# 31256 KB / 44 ms
import sys
P,M = map(int,sys.stdin.readline().split())  # P : 플레이어 수, M : 방 한 개의 정원
total_room=[]   # 전체 방
for _ in range(P):
    l,N = map(str,sys.stdin.readline().split())  # l : 플레이어 레빌 , N : 플레이어 닉네임
    L=int(l)
    for t in range(len(total_room)):  # 방을 하나 씩 돌면서 조건문 확인
        # t 방에 처음 들어온 사용자의 레벨과의 차이가 10이하 이고, t방에 들어와 있는 사람 수가 정원보다 작을 때 추가
        if (abs(int(total_room[t][0][0])-L)<=10) and (len(total_room[t])<M) :
            total_room[t].append((l,N))
            break
    else :  # 모든 방에 들어갈 수 없다면, 새로운 방 생성
        total_room.append([(l,N)])
        
for room in total_room:  
    if len(room)==M: print("Started!")  # 정원이 차있다면 Started! 출력
    else: print("Waiting!")  # 대기 중이라면 Waiting! 출력
    for n in sorted(room,key = lambda x: x[1]):  # 이후, 닉네임을 기준으로 정렬한 후, 출력
        print(n[0],n[1])
    
    
