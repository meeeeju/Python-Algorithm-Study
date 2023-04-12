#블로그보니 이렇게 간단한걸 너무 복잡하게 생각했다..
#메모리 :31256 #시간 :44ms
S=list(input())
for i in range(len(S)):
    if S[i:]==S[i:][::-1]:
        print(len(S)+i)
        break
'''
start=len(S)//2
liist=[]
liist2=[]
liist3=[]
liist4=[]
drom1=False
drom2=False
for i in range(start,len(S)):
    
    liist=S[0:i]
    liist2=S[i+1:len(S)]
    liist=liist[::-1]
    #print(liist)
    #print(liist2)
    
    count1=0
    for j in range(min(len(liist),len(liist2))):
        if liist[j]!=liist2[j]:
            break
        count1+=1
        if count1!=0:
            count1=max(len(liist),len(liist2))-count1
        else:
            drom1=False
            break
    #print(count1)
    liist3=S[0:i+1]
    liist4=S[i:len(S)]
    liist3=liist3[::-1]
    print(liist3)
    print(liist4)
    count2=0
    for j in range(min(len(liist3),len(liist4))):
        
        if liist3[j]==liist4[j]:
            count2+=1
        else :
            count2=0
            break
        print(count2)

    if count2!=0:
        count2=max(len(liist3),len(liist4))-count2
    else:
        drom2=False
        break
    print(count2)
    '''

