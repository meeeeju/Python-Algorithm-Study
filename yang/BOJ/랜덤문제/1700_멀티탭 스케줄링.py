# 어떻게 푸는지 모르겠어서 블로그 참고
# 31120KB / 40ms

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use_order = list(map(int, input().split()))

plug = set()
count = 0
for i in range(0, K):
    if use_order[i] in plug:
        continue
    elif len(plug) < N:
        plug.add(use_order[i])
    else: # 플러그에서 하나 빼야함 => 가장 나중에 나오는 것 빼기
        plug_check = plug.copy()
        for j in range(i + 1, K):
            item = use_order[j]
            if len(plug_check) == 1: # 가장 나중에 등장한 plug
                plug.remove(plug_check.pop())
                break
            if item in plug_check:
                plug_check.remove(item)
        else: # for 문을 끝가지 돌았다 == plug_check 의 사이즈가 1 보다 크다 == 더이상 나오지 않는 아이템이 있다
            plug.remove(plug_check.pop())
        plug.add(use_order[i])
        count += 1
print(count)