N=int(input())
counts={}
liist=[]

for i in range(N):
    book=input()
    
    if book not in counts: #input 받은 book중에
        counts[book]=1 #counts중에 없으면 갯수 1
    else:
        counts[book]+=1 #counts중에 있으면 갯수 +1

maxx=max(counts.values()) #counts중 max갯수 구하기

for i in counts:
    if maxx==counts[i]: #max 갯수랑 같은 애들 liist에 append
        liist.append(i)

if len(liist)==1: #liist 길이가 1이면 그냥 출력
    print(liist[0])
else:
    liist.sort() #liist 길이가 여러개이면 사전순으로 정렬해서 출
    print(liist[0])