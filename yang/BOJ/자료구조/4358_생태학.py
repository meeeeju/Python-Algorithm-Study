# 31256KB / 480ms
# 블로그 참고
import sys
input = sys.stdin.readline
trees = {}
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    n += 1
treeList = sorted(trees.keys())
for tree in treeList:
    print(f"{tree} {(trees[tree]/n)*100:.4f}")