word = input()
c_dict = {key: 0 for key in 'abcdefghijklmnopqrstuvwxyz'}
for c in word:
    c_dict[c] += 1
for k, n in c_dict.items():
    print(n, end=' ')
