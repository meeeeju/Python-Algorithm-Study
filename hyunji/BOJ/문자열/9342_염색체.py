import sys
input=sys.stdin.readline

t=int(input())
true=0
false=0

for i in range(t):
    string=list(input())
    acount=0
    fcount=0
    ccount=0
    abcdefcount=0   
    if string[0]=='A':
        if string[1]=='A' or string[1]=='F':
            for j in range(1,len(string)):
                if string[j]=='A':
                    acount+=1
                elif string[j]=='F':
                    fcount+=1

        else:
            false+=1
            #print("Good")
            #break
        if fcount==0:
            false+=1
            #print("Good")
            #break
        else:
            if string[acount+fcount+1]=='C':
                for j in range(acount+fcount+1,len(string)):
                    if string[j]=='C':
                        continue
                    elif string[j]=='A' or string[j]=='B' or string[j]=='D' or string[j]=='E' or string[j]=='F':
                            abcdefcount+=1
                            if abcdefcount>2:
                                false+=1
                                #print("Good")
                                #break
                    else:
                        false+=1
                        #print("Good")
                        #break
            else:
                false+=1
                #print("Good")
                #break
        if false==0:
            print("Infected!")
        else:
            print("Good")
    
        
    else:
        if string[1]!='A':
            false+=1
        else:
            if string[2]=='A' or string[2]=='F':
                for j in range(2,len(string)):
                    if string[j]=='A':
                        acount+=1
                    elif string[j]=='F':
                        fcount+=1
                    

            else:
                false+=1
                #print("Good")
                #break
            if fcount==0:
                false+=1
                #print("Good")
                #break
            else:
                if string[acount+fcount+2]=='C':
                    for j in range(acount+fcount+1,len(string)):
                        if string[j]=='C':
                            continue
                        elif string[j]=='A' or string[j]=='B' or string[j]=='D' or string[j]=='E' or string[j]=='F':
                            abcdefcount+=1
                            if abcdefcount>2:
                                false+=1
                                #print("Good")
                                #break
                        else:
                            false+=1
                            #print("Good")
                            #break
                else:
                    false+=1
                    #print("Good")
                    #break
            #print("Infected!")
        if false==0:
            print("Infected!")
        else:
            print("Good")
