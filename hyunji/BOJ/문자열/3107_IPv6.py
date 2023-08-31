import sys
input=sys.stdin.readline
ip=list(input().strip())
liist=[]
col=[]
result=[]
for i in range(len(ip)):
    if ip[i]==':':
        col.append(i)
a=0
for i in col:
    liist.append(ip[a:i])
    a=i+1
liist.append(ip[col[-1]+1:])


putzero=0
for i in range(len(liist)):
    if len(liist[i])==0:
        putzero=i

for i in range(len(liist)):
    if len(liist[i])==4:
            result.append(liist[i])
            continue

    elif len(liist[i])==0:
        result.append(['0','0','0','0'])
        continue
    else:
        for j in range(len(liist[i])):
            sublist=[]
            zero=4-len(liist[i])
            for _ in range(zero):
                sublist.append('0')
            for k in liist[i]:
                sublist.append(k)
            result.append(sublist)
            break
result2=[]

if len(result)==7:
    for i in result:
        for j in i:
            result2.append(j)

else:
    for i in range(len(result)):
        if i==putzero:
            result2.append(result[i])
            for j in range(8-len(result)):
                result2.append(['0','0','0','0'])
        else:
            result2.append(result[i])
        
    
    #for i in result:
        #result2.append(i)

result2=sum(result2,[])

result3=[]
for i in range(len(result2)):
    if i==4 or i==8 or i==12 or i==16 or i==20 or i==20 or i==24 or i==28:
        result3.append(':')
        result3.append(result2[i])
    else:
        result3.append(result2[i])

for i in result3:
    print(i,end='')
