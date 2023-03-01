import sys
input=sys.stdin.readline
tree=dict()
count=0

while 1:
    kind=input().rstrip()
    
    if kind=='':
        break
    
    count+=1
    
    if kind in tree:
        tree[kind]+=1
    else:
        tree[kind]=1
        
treelist=dict(sorted(tree.items()))

for i in treelist:
    percent=(treelist[i]/count)*100
    print("%s %.4f" %(i,percent))
    
