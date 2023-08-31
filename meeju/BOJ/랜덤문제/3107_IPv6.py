# 31256	48
import sys
input = sys.stdin.readline

'''예외 처리해주기'''

'''
25:09:1985:aa:091:4846:374:bb'''

ipv6 = input().rstrip()
partions = ipv6.split("::")

result = []
cnt = 0

for part in partions:
    if not part:
        result.append([])
        continue
    temp = part.split(":")
    cnt += len(temp)

    for i in range(len(temp)):
        size = len(temp[i])
        add = ''
        while size < 4:
            add += '0'
            size+=1
        temp[i]= add + temp[i]
    result.append(temp)

group0=[]
for i in range(8-cnt):
    group0.append('0000')

if cnt ==8:
    IPV6 = result[0]
else:
    IPV6 = result[0] + group0 + result[1]

print(*IPV6,sep=':')



