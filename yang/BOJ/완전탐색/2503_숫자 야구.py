# 31256KB / 40ms
# 왜 틀린지 몰라서 질문게시판 참고
# 알고보니 범위 착각했었음 012 이런것도 되는줄,, 1~9까지에서 고르는거였어
# 그리고 수 중복으로 고르면 안되는것도 몰랐음..
import sys
input = sys.stdin.readline

def check(number, q): # number가 questions[q] 조건 성립하는지 검사
    s, b = 0, 0
    s_number = str(number)
    # s_number = str(number).zfill(3)
    for i in range(3):
        if questions[q][0][i] == s_number[i]:
            s += 1
    for i in range(3):
        if s_number[i] in questions[q][0]:
            b += 1
    b -= s
    if s==questions[q][1] and b==questions[q][2]:
        return True
    return False

n = int(input())
questions = []
for _ in range(n):
    number, s, b = input().split()
    questions.append((number, int(s), int(b)))

numbers = []
for i in range(1, 10): # 첫번째 자리
    for j in range(1, 10): # 두번째 자리
        if i==j: continue
        for k in range(1, 10): # 세번째 자리
            if i==k or j==k: continue
            numbers.append(i+10*j+k*100)
ans = 0
# ans_list = []
for number in numbers:
    for i in range(n):
        if not check(number, i):
            break
    else:
        ans += 1
        # ans_list.append(number)
# print(*ans_list)
print(ans)