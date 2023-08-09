# 31256KB / 40ms
K = int(input())

size = 1
while size < K:
    size *= 2
if size == K :
    print(size, 0)
    exit(0)
present_size = size
count = 0
while K > 0:
    present_size //= 2 # 쪼갬
    count += 1
    if K >= present_size: # 상근이가 가져감
        K -= present_size

print(size, count)