# 1%에서 틀림
# 질문게시판에 반례 몇개 없지만 그건 일단 다 돌아감..
from sys import stdin
sinput = stdin.readline

def windowCompareTo(fileName1:str, fileName2:str):
    '''
    1 : fileName1 > fileName2
    0 : fileName1 == fileName2
    -1 : fileName1 < fileName2
    '''
    fp1, fp2 = 0, 0
    while fp1<len(fileName1) and fp2<len(fileName2):
        if fileName1[fp1].isalpha() and fileName2[fp2].isalpha(): # 둘다 알파벳
            if fileName1[fp1].lower() == fileName2[fp2].lower(): # 같은 알파벳 => 대문자가 앞
                if fileName1[fp1] == fileName2[fp2]:
                    fp1 += 1
                    fp2 += 1
                elif fileName1[fp1].islower(): return -1
                else: return 1
            else: # 서로 다른 알파벳 => ABC 순서 빠른거
                if fileName1[fp1].lower() < fileName2[fp2].lower(): return -1
                else: return 1
        elif fileName1[fp1].isalpha() and fileName2[fp2].isdigit():
            return -1
        elif fileName1[fp1].isdigit() and fileName2[fp2].isalpha():
            return 1
        else: # 숫자 숫자
            f1num, f2num = "", ""
            while fp1<len(fileName1):
                if fileName1[fp1].isdigit():
                    f1num += fileName1[fp1]
                    fp1 += 1
                else: break
            while fp2<len(fileName2):
                if fileName2[fp2].isdigit():
                    f2num += fileName2[fp2]
                    fp2 += 1
                else: break
            if int(f1num) < int(f2num) : return 1
            elif int(f1num) > int(f2num) : return -1
            else:
                if len(f1num) > len(f2num): return -1
                elif len(f1num) < len(f2num): return 1
    if fp1 == len(fileName1) and fp2 == len(fileName2): return 0
    if fp1 < len(fileName1): return -1
    return 1

def quick_sort_with_window(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        compare = windowCompareTo(num, pivot)
        if compare == 1: # num < pivot
            lesser_arr.append(num)
        elif compare == -1: # num > pivot
            greater_arr.append(num)
        else: # num == pivot
            equal_arr.append(num)
    return quick_sort_with_window(lesser_arr[:]) + equal_arr + quick_sort_with_window(greater_arr[:])


N = int(input())
fileNameList = []
for _ in range(N):
    fileNameList.append(input().rstrip())

print("\n".join(quick_sort_with_window(fileNameList)))