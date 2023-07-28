#31256KB / 44ms
import sys
input = sys.stdin.readline
ans = []
N = int(input())
for _ in range(N):
    string = input().rstrip()
    temp = ''
    for i in range(len(string)):
        if string[i].isdigit():
            temp += string[i]
        elif temp != '':
            ans.append(int(temp))
            temp = ''
        if i == len(string)-1 and temp != '':
            ans.append(int(temp))
            temp = ''
ans.sort()
for a in ans:
    print(a)