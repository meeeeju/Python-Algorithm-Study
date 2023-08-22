# 31256KB / 52ms
from sys import stdin
input = stdin.readline

N = int(input())
array = list(map(int, input().split()))
s = int(input())
target = 0
change = 0
while s >= 0 and target<N:
    sorted_array_with_index = sorted(enumerate(array[target:]), key=lambda x:x[1], reverse=True)
    for i in range(len(sorted_array_with_index)): # find change index
        if sorted_array_with_index[i][0] <= s:
            s -= sorted_array_with_index[i][0]
            change = target+sorted_array_with_index[i][0]
            break
    while change > target: # bubble sort
        array[change], array[change-1] = array[change-1], array[change]
        change -= 1
    target += 1 # find target
print(*array)