# 시간초과가 나서 블로그 코드랑 비교하다가 조합 구하는 함수(select_alpha)를 itertools로 바꿔봤는데 그랬더니 맞음.
# 왜 그러지??
# 165400KB / 1376ms (PyPy3)
# 79032KB / 2120ms (Python3)

import sys
from itertools import combinations 

input = sys.stdin.readline

def calcul_readable_words(la):
    count = 0
    for word in words:
        for w in word:
            if w not in la:
                break
        else:
            count += 1
    return count

N, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    words = []
    learned_alpha = set(['a', 'n', 't', 'a', 't', 'i', 'c', 'a'])
    learnable_alpha = set()
    for _ in range(N):
        word = input().rstrip()[4:][:-4]
        words.append(word)
        for w in word:
            if w not in learned_alpha:
                learnable_alpha.add(w)

    if k >= len(learnable_alpha):
        print(N)
    else:
        learnable_alpha = list(learnable_alpha)
        ans = 0
        for teach in list(combinations(learnable_alpha, k)):
            ans = max(ans, calcul_readable_words(set(teach)|learned_alpha))
        print(ans)

#### 시간 초과 나는 코드 ####
'''
import sys
input = sys.stdin.readline

def select_alpha(x):
    if x == k:
        global ans
        ans = max(ans, calcul_readable_words(set(learned_alpha)))
        return
    for i in range(x, len(learnable_alpha)):
        learned_alpha.append(learnable_alpha[i])
        select_alpha(x + 1)
        learned_alpha.pop()

def calcul_readable_words(la):
    count = 0
    for word in words:
        for w in word:
            if w not in la:
                break
        else:
            count += 1
    return count

N, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    words = []
    learned_alpha = set(['a', 'n', 't', 'a', 't', 'i', 'c', 'a'])
    learnable_alpha = set()
    for _ in range(N):
        word = input().rstrip()[4:][:-4]
        words.append(word)
        for w in word:
            if w not in learned_alpha:
                learnable_alpha.add(w)

    if k >= len(learnable_alpha):
        print(N)
    else:
        learned_alpha = list(learned_alpha)
        learnable_alpha = list(learnable_alpha)
        ans = 0
        select_alpha(0)
        print(ans)
'''