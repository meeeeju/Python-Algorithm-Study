import sys
input=sys.stdin.readline

n=int(input())
box=[0]*1000
box[1]=1
box[2]=2
for i in range(3,1000):
    box[i]=box[i-1]+box[i-2]
print(box[n]%10007)
