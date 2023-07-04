# 블로그 참고
# https://latte-is-horse.tistory.com/373
# 31256KB / 80ms
nums = input()
i = 1
while True:
    numI = str(i)
    while len(numI) > 0 and len(nums) > 0:
        if numI[0] == nums[0]:
            nums = nums[1:]
        numI = numI[1:]
    if nums == '':
        print(i)
        break
    i += 1