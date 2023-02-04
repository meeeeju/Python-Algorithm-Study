import sys
n = int(input())
counter = {} # 개수 세기
m = 0
ans = {} # 정답 집합
for i in range(n):
    book = sys.stdin.readline()
    if book in counter:
        counter[book] += 1
    else:
        counter[book] = 1
    if counter[book] > m:
        ans = {book}
        m = counter[book]
    elif counter[book] == m:
        ans.add(book)
print(sorted(list(ans))[0])