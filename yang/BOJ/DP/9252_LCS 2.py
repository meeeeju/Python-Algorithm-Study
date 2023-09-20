# 블로그 참고
# 486512KB / 700ms (PyPy3)
import sys
input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
lcs = [[''] * len(s2) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            if i >= 1 and j >= 1:
                lcs[i][j] += lcs[i-1][j-1]
            lcs[i][j] += s1[i]
        else:
            if i >= 1 and len(lcs[i][j]) < len(lcs[i-1][j]):
                lcs[i][j] = lcs[i-1][j]
            if j >= 1 and len(lcs[i][j]) < len(lcs[i][j-1]):
                lcs[i][j] = lcs[i][j-1]

print(len(lcs[-1][-1]))
print(lcs[-1][-1])
