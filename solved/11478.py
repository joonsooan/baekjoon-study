# s = input()

# sub_str_length = 1
# sub_string_dict = {}
# for j in range(len(s)):
#     for i in range(len(s) - sub_str_length + 1):
#         new_sub_string = s[i: i + sub_str_length]
#         if sub_string_dict.get(new_sub_string) == None:
#             sub_string_dict[new_sub_string] = 1
#     sub_str_length += 1

# print(len(sub_string_dict))

s = input()
total = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        total.add(s[i:j+1])

print(len(total))
