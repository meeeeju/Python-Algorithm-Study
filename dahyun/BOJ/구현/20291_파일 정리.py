import sys
input = sys.stdin.readline
extension = dict()
for _ in range(int(input())):
    file = input().strip().split('.')[1]
    if file in extension: extension[file]+=1
    else: extension[file]=1
for item in sorted(extension.items(),key= lambda item : item[0]):
    print(item[0],item[1])
    
