# 31388kb /	44ms
import sys
input = sys.stdin.readline
'''
10 5
10 a
15 b
20 c
25 d
30 e
17 f
18 g
26 h
24 i
28 j'''
p, m = map(int, input().split())    # p : 플레이어의 수, m : 방 정원 갯수

room={}
detail_info_room={}

def joinRoom(level,name):

    for i in room.keys():
        if i[0]-10 <= level <= i[0]+10:
            if detail_info_room[i[1]] <  m :
                room[i].append((level,name))    # 방에 가입시켜주기
                detail_info_room[i[1]] +=1      # 인원 수 업데이트시키기
                return True
    return False
            
def created_room(level,name):
    room[(level,name)]=[(level,name)]   #  key 값을 (level, name )으로 value 값에 이름 넣어서 반환
    detail_info_room[name]= 1
    return 

def main():

    for i in range(p):
        level , name = input().split()
        level = int(level)

        if not joinRoom(level,name):    # 매칭 가능한 방이 없다면
            created_room(level,name)

    for manager, members in room.items():
        members.sort(key = lambda x :x[1])
        if detail_info_room[manager[1]] == m:
            print("Started!")     
        else:
            print("Waiting!")
        for level,member in members:
                print(level, member)    

main()

