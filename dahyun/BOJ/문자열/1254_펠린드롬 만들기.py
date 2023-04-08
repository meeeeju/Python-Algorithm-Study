#BaekJoon 1254 펠린드롬 만들기
# 31388 KB / 40 ms
# 20분
import sys
def check(start,end):  # start ~ end 까지 팰린드롬인지 확인
    while start<end:
        if (start>=size or 0>end) : return False
        if S[start]!=S[end]: return False
        start+=1
        end-=1
    return True
S = sys.stdin.readline().strip()  # 문자
size= len(S)  # 문자 전체 크기
for i in range(size):
    if S[i]==S[-1] and check(i,size-1):  # 마지막 문자와 동일 & 해당 값부터 마지막까지 팰린드롬
        print(size+(size-(size-i)))  # 전체 크기 + (전체크기에서 (i~끝) 빼준 값)
        break
