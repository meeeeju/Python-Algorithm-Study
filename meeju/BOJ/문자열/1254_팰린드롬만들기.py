# 37048kb /	96ms	
import sys
from queue import Queue
input = sys.stdin.readline

'''
1. 팰린드롬이 되는 구간을 찾는다.
2. 아닌 구간의 문자열의 길이를 계산한다..
주의 :  S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬 ( 문자열 뒤에 추가해야됨)
'''

# 이중 for 문 돌리기 
def is_pallendrome(s):
    if s[::-1]==s:
        return True
    return False

S = input().rstrip()
init_len = len(S)

def make_pallendrome(S):
    result =[]
    for i in range(init_len-1):
        if is_pallendrome(S[i::]):
            return i+init_len
    return 2*init_len-1
answer = make_pallendrome(S)

print(answer)