l = int(input())
string = list(input())
a_dict = {chr(i): i-96 for i in range(97, 123)}
r, M = 31, 1234567891
ans = 0

for i in range(len(string)):
    a_dict[string[i]]
    x = (a_dict[string[i]] * (r**i)) % M
    ans = (ans + x) % M

print(ans)
