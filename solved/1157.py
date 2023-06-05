word = input().upper()
word_dict = {}

for char in word:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1

keys_list = []
for keys in word_dict.keys():
    keys_list.append(keys)
values_list = word_dict.values()

max_value = max(values_list) 
list = [x for x, y in enumerate(values_list) if y == max_value]

if len(list) == 1:
    print(keys_list[int(list[0])])
else:
    print("?")