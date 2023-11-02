word = input()
word_list = list(word)
min_time = 0

for char in word_list:
    if char in "ABC":
        min_time += 3
    elif char in "DEF":
        min_time += 4
    elif char in "GHI":
        min_time += 5
    elif char in "JKL":
        min_time += 6
    elif char in "MNO":
        min_time += 7
    elif char in "PQRS":
        min_time += 8
    elif char in "TUV":
        min_time += 9
    elif char in "WXYZ":
        min_time += 10

print(min_time)