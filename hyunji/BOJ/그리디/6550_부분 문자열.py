#메모리 :31956 시간 :60
import sys
input=sys.stdin.readline
while True:
    try:
        s,t=input().split()
        s=list(s)
        t=list(t)
        liist=[]
        here=0

        if len(s)>len(t):
            print("No")
        else:
            j=0
            
            liist=[]
            for i in range(len(t)):
                if t[i]==s[j]:
                    liist.append(t[i])
                    j+=1
                    if len(liist)==len(s):
                        print("Yes")
                        break
            if len(liist)!=len(s):
                print("No")
              '''
              for i in range(len(s)):
                for j in range(len(t)):
                    if len(liist)==len(s):
                        break
                    elif s[i]==t[j]:
                        liist.append(t[j])
                        if s[i]!=liist[-1]:
                            print("No")
                            break
                        s[i]=0
                        here=j
                    for k in range(here+1):
                        t[k]=1
                    
                    
            if len(liist)==len(s):
                print("Yes")
            else:
                print("No")'''
    except:
        break
