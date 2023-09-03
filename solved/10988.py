def palindrome(s):
    i = 0
    while i < len(s) // 2:
        if s[i] != s[len(s) - i - 1]:
            return 0
        i += 1
    return 1


s = input()
print(palindrome(s))
