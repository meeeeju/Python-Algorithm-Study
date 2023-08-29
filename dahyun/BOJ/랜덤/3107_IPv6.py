#31256KB/	40ms

result = [['0','0','0','0'] for _ in range(8)] # 초기화

IPv6 = input() # 올바른 축약형 IPv6주소

count=0 # IPv6의 몇 번째 인덱스인지
zero=False # :: 인지 아닌지
temp='' # 숫자들 모음 ( : 을 기준으로)

for i in range(len(IPv6)):                    # IPv6를 하나씩 돌림
    if IPv6[i]!=':': temp+=IPv6[i]            # 숫자면, temp에 저장
    else :                                    # : 값
        if IPv6[i-1]==':' or i==0: zero=True  # 만약 이전 값이 : 이거나 , :으로 시작하는데 처음일 때 (ex. ::1)
        
        if zero :                             # ::일 때,
            digit = IPv6[i+1:].split(':')     # :: 는 한 번만 나오므로, 이후 값들을 :로 분리
            count = 8-len(digit)              # count는 8개의 인덱스에서, 이후 값 (digit의 길이) 빼기
            zero=False                        # ::는 이제 끝~!
            
        else:                                 # :일 때,
            temp_j=3                          # IPv6의 하나의 인덱스는 4bit이므로, temp_j = 3
            for j in range(len(temp)-1,-1,-1):# j - 숫자들 앞에 0이 들어와야하므로, 뒤에서부터 보기 ! (ex. 12 -> 0012)
                result[count][temp_j]=temp[j] # result[현재 인덱스][4bit 중 인덱스] = 숫자들(temp)[j]
                temp_j-=1                     # 뒤에서부터 앞으로 가므로 -=1
            temp=''                           # 모아둔 숫자들은 result에 초기화했으므로 temp도 초기화해줌
            count+=1                          # 인덱스 숫자 증가
            
    if i==len(IPv6)-1:                        # i가 마지막 인덱스일 때,
        temp_j=3
        for j in range(len(temp)-1,-1,-1):
            result[count][temp_j]=temp[j]
            temp_j-=1
        temp=''
        count+=1
     
for r in range(len(result)):
    print(result[r][0]+result[r][1]+result[r][2]+result[r][3],end='')
    if r!=len(result)-1: print(":",end='')
