#블로그 참고
'''
liist=[]
for i in range(len(n)):
    liist.append(int(n[i]))
maxx=liist[0]'''

nums = input()
i = 0
while True:
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        num = num[1:]
    if nums == '':
        print(i)
        break

'''
for i in range(1,len(liist)):
    if liist[i]>liist[i-1]:
        maxx=liist[i]+(maxx//10)*10
    elif liist[i]<=liist[i-1]:
        if maxx>liist[i]*10+liist[i+1]:
            maxx=liist[i]*10+liist[i+1]
        else:
            maxx=10*((maxx//10)+1)
            maxx+=liist[i]
        
        
    print(maxx)'''
