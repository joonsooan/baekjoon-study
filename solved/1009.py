arr = [
    [0],
    [1],
    [6, 2, 4, 8],
    [1, 3, 9, 7],
    [6, 4],
    [5],
    [6],
    [1, 7, 9, 3],
    [6, 8, 4, 2],
    [1, 9],
    [10]
]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a_end = a % 10
    if a_end == 0:
        print(10)
    elif a_end in [1, 5, 6]:
        print(a_end)
    elif a_end in [4, 9]:
        print(arr[a_end][b % 2])
    else:
        print(arr[a_end][b % 4])
