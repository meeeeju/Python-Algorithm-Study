# 52036	240
import sys
input = sys.stdin.readline

'''
8 파일의 개수
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
'''

file_num  = int(input())
file_list = [0 for _ in range(file_num)]
extension_archive ={}

for i in range(file_num):
    file_list[i] = input().rstrip().split('.')

for word,extension in file_list:
    if extension in extension_archive.keys():
        extension_archive[extension]+=1
    else:
        extension_archive[extension]=1


result = list(extension_archive.items())
result.sort(key=lambda x: x[0])
for i in result:
    print(*i)

# print(*sorted(result,key = lambda x: x[0]))

# print(result)