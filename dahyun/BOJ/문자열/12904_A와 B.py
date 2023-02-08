import sys
    
S=sys.stdin.readline().strip()
T=sys.stdin.readline().strip()

while True:
    if len(T)==len(S): break # T와 S의 문자열 길이가 같다면 break
    last = T[-1]  # last : T의 문자열 마지막 문자
    T=T[:-1]  # T에 마지막 문자를 제거
    if last=='B': T=T[::-1]  # last가 B면 T의 문자열을 뒤집는다
    
if T==S : print(1)  # T와 S의 문자열이 같다면 1 출력
else : print(0)
