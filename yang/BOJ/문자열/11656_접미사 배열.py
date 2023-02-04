s = input()
sList = sorted([s[i:] for i in range(len(s))])
print('\n'.join(sList))