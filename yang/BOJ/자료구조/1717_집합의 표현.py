# 125048KB / 4632ms (PyPy3)
import sys
input = sys.stdin.readline

def root(a):
    while a != tree[a]:
        a = tree[a]
    return a

n, m = map(int, input().split())
tree = [i for i in range(n+1)]
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        tree[root(b)] = root(a)
    else:
        if root(a)==root(b):
            print("YES")
        else:
            print("NO")