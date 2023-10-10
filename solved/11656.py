s = input()
suffix_lst = []

for i in range(len(s)):
    suffix_lst.append(s[i:])
suffix_lst.sort()

for s in suffix_lst:
    print(s)
