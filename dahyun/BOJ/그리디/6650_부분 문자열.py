#31256KB/	72ms
import sys
input = sys.stdin.readline

while True:
    try:
        s,t = map(str,input().split())
        now=0  # s의 현재 인덱스
        result=0  # 결과 - true, no
        for i in range(len(t)):
            if s[now]==t[i]: now+=1  # 만약 s의 값과 t의 값이 같으면 now(현재 인덱스) 증가
            if now==len(s): print("Yes"); result=1; break; # now가 s의 끝을 가리키면, s가 t에 포함되어있다고 증명되는 것 !
        if not result: print("No")
    except Exception:
        break
