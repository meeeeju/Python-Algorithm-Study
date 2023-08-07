#37920KB/	120ms
import sys
from queue import Queue 
input=sys.stdin.readline
for _ in range(int(input())):
    count=1
    Q = Queue()
    N,M = map(int,input().split())  # 문서개수 / 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수
    nlist = list(map(int,input().split())) # 문서의 중요도
    for i in range(len(nlist)):
        Q.put((nlist[i],i)) # 중요도, 순서
    while Q.qsize() :
        q=Q.get()
        if q[0]<max(nlist): Q.put((q[0],q[1])) # 중요도가 가장 크지 않으면 다시 재배치
        elif q[1]==M : # 같은 위치
            print(count)
            break
        else : # 가장 큰 중요도 문서 인쇄 (삭제)
            count+=1
            nlist.remove(q[0])
    
