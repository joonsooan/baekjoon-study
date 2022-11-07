N = int(input())
total_num = 0

def is_prime_number(n):
    if n == 1:
        return False


    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = input().split()

for i in range(N):
    num = int(numbers[i])
    if is_prime_number(num):
        total_num += 1

print(total_num)