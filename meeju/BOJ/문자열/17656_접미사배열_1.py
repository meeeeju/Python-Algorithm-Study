import sys
''' 
 입력:   baekjoon
 출력: 
        aekjoon
        baekjoon
        ekjoon
        joon
        kjoon
        n
        on
        oon
'''
input= sys.stdin.readline
S=input().rstrip()
dic=[]

for i in range(len(S)):
    dic.append(S[i:len(S)])
    
dic.sort()
for s in dic:
    print(s)

# #풀이과정
# 파이썬의 slicing 을 알면 쉽게 접근가능하다
# S[i:len(S)] : i부터 끝까지로 된 새로운 리스트 
# 튜플, range, 문자열도 시퀀스 자료형이므로 리스트와 같은 방식으로 슬라이스를 사용할 수 있다
