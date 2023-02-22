# 40144KB / 6148ms

import sys
input = sys.stdin.readline
import math
from queue import Queue


def is_primeNumber(a):  # 소수인지 아닌지 판별하는 함수
    for i in range(2,int(math.sqrt(a))+1):
        if not (a % i):
            return False
    return True


def bfs(A,B):
    queue = Queue()
    queue.put((A,0))
    visited = []   # 방문 기록 여부

    while(queue.qsize()>0):
        num,count = queue.get()

        if num == B:
            print(count)
            return count

        visited.append(num)

        digit_number = [int(str(num)[0]),int(str(num)[1]),int(str(num)[2]),int(str(num)[3])]
        combi_list =[]


        # case 1 첫번째 자리 수 바꾸기
        for i in range(1,10):
            combi = 1000 * i + 100 * digit_number[1] + 10 * digit_number[2] + digit_number[3]
            combi_list.append(combi)
            # if is_primeNumber(combi):
            #     queue.put(combi,v[1]+1)
        
        # case 2 두번째, 세번째  자리 수 바꾸기
        for i in range(0,10):     
            combi = 1000 * digit_number[0] + 100 * i + 10 * digit_number[2] + digit_number[3]
            combi_list.append(combi)
            combi = 1000 * digit_number[0] + 100 * digit_number[1] + 10 * i + digit_number[3]
            combi_list.append(combi)
            # if is_primeNumber(combi):
            #     queue.put(combi,v[1]+1)

        # case 3 네번째 자리 수 바꾸기 (홀수만 하면 됨)
        for i in range(1,10,2):
            combi = 1000 * digit_number[0] + 100 * digit_number[1] + 10 * digit_number[2] + i
            combi_list.append(combi)
        
        combi_list= list(set(combi_list)-set(visited))  # 중복되는 것 다 걸러주기
        for combi in combi_list:
        
            if is_primeNumber(combi):
                queue.put((combi,count+1))

    print("impossible")
    return -1

testcase = int(input())
for _ in range(testcase):
    A,B = map(int,input().split())

    bfs(A,B)
    
