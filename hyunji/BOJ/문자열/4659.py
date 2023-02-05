moeum={'a','e','i','o','u'}
while True:
    test_case=input()
    if test_case=='end':
        break
    
    spell=list(test_case)
    error=0
    mo=0
    mo3=0
    ja3=0
    
    for i in range(len(spell)):
        if i>0:
           if spell[i-1]==spell[i]:
                if spell[i]!='e' and spell[i]!='o':
                    error+=1
        if spell[i] in moeum:
                mo=1
                mo3+=1
                ja3=0
                if mo3==3:
                    error+=1
            
        else:
            mo3=0
            ja3+=1
            if ja3==3:
                error+=1
    
    if error==0 and mo==1:
        print("<"+ test_case +"> is acceptable.")
    else:
        print("<"+ test_case +"> is not acceptable.")
                    