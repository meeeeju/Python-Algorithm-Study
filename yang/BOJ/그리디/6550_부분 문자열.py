# 31256KB / 192ms
# 예외처리 질문게시판 참고!
from sys import stdin
input = stdin.readline

while True:
    try:
        s, t = input().rstrip().split()
        isSubsequence = False
        for find_index in range(len(t)-len(s)+1):
            if t[find_index]==s[0]:
                t_index = find_index
                s_index = 0
                while t_index < len(t) and s_index < len(s):
                    if t[t_index]==s[s_index]:
                        s_index += 1
                    t_index += 1
                if s_index==len(s):
                    isSubsequence = True
                    break
        if isSubsequence:
            print("Yes")
        else:
            print("No")
    except Exception:
        break