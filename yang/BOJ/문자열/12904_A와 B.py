# a*로 풀다가 자꾸 시간초과나서
# 질문게시판의 글 보고 풀었습니다..
# https://www.acmicpc.net/board/view/83783
S = input()
T = input()
while len(T) > len(S):
    if T[-1]=="A":
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
if S == T:
    print(1)
else:
    print(0)