#  블로그 참고
n=int(input())
liist=[]
result=[]
number=["0","1","2","3","4","5","6","7","8","9"]


for _ in range(n):
    string=list(input().rstrip())
    
    word=""
    result2=[]
    for i in string:
        if i in number:
            word+=i
        else:
            if word:
                result2.append(int(word))
                word=""

    if word:
        result2.append(int(word))
        word=""
    result.append(result2) 

result.sort()
for i in result:
    print(i)
