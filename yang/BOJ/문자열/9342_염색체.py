# 31256KB / 40ms
from sys import stdin
sinput = stdin.readline

def check_pattern(string):
    i = 0
    if string[0] not in {"A","B", "C", "D", "E", "F"}: return False
    i += 1
    while i < len(string)-1:
        if   string[i]=="A": i += 1
        elif string[i]=="F": break
        else: return False
    while i < len(string)-1:
        if   string[i]=="F": i += 1
        elif string[i]=="C": break
        else: return False
    while i < len(string)-1:
        if   string[i]=="C": i += 1
        else: break
    if i < len(string)-1: return False
    return string[-1] in {"A", "B", "C", "D", "E", "F"}

T = int(sinput())
for _ in range(T):
    string = sinput().rstrip()
    if check_pattern(string):
        print("Infected!")
    else:
        print("Good")