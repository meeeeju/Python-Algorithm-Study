#58920kb /	184ms
import sys
input = sys.stdin.readline

'''
5 2
1 4 2 5 1'''

N, X = map(int,input().split())     # N : 블로그를 시작하고 지난 일 수, X : 기간
visit = list(map(int,input().split()))

# start = 0
# end = X-1

if max(visit):
    max_visitor = sum(visit[0:X])
    temp = sum(visit[0:X])
    max_cnt = 0 
    for i in range(N-X+1):
        # start = i
        # end = i+X-1
        if i != 0:
            temp = temp - visit[i-1] + visit[i+X-1]
        if temp < max_visitor :
            continue
        elif temp > max_visitor :
            max_visitor = temp
            max_cnt = 1
        else:
            max_cnt += 1
    print(max_visitor,max_cnt,sep='\n')
else:
    print("SAD")


''''
"블로그"문제에서 투포인터를 사용해야하는 이유
리스트에서 부분 문자여'''

# if max(visit):

#     max_visitor = sum(visit[0:X])
#     max_cnt = 0 
#     for  i in range(N-X+1):
#         new = sum(visit[i:i+X])
#         if new < max_visitor :
#             continue
#         elif new > max_visitor :
#             max_visitor = new
#             max_cnt = 1
#         else:
#             max_cnt += 1
#     print(max_visitor)
#     print(max_cnt)
# else:
#     print("SAD")
