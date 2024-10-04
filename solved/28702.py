a = input()
b = input()
c = input()
lst = [a, b, c]
x = 4
next_num = 0

for i in lst:
    x -= 1
    if (i != "Fizz" and i != "Buzz" and i != "FizzBuzz"):
        next_num = int(i) + x
        if next_num % 15 == 0:
            print("FizzBuzz")
        elif next_num % 3 == 0:
            print("Fizz")
        elif next_num % 5 == 0:
            print("Buzz")
        else:
            print(next_num)
        break
    else:
        pass
