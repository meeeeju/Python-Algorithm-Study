#블로그 참고
string=input().rstrip()
pokbal=input().rstrip()
liist=[]

for i in range(len(string)):
    liist.append(string[i])
    if ''.join(liist[-len(pokbal):])==pokbal:
        for _ in range(len(pokbal)):
            liist.pop()
if liist:
    print(''.join(liist))
else:
    print("FRULA")

'''
for i in range(len(string)-1,-1,-1):
    if string[i]==pokbal[-1]:
        if ''.join(string[-len(pokbal):])==pokbal:
            for _ in range(len(pokbal)):
                string.pop()
print(string)'''
        
