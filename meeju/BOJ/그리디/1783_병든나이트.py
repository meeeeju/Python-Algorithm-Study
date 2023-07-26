# 	31388	40
import sys
input = sys.stdin.readline


'''
세로 길이 N와 가로 길이 M
100 50'''

N, M = map(int,input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min((M+1)//2,4))
else:   # N >=3 
    if M < 7 :
        print(min(M,4))
    else:
        print(5+M-7) # 4 + M -7
