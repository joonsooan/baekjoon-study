import sys


n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

# 버블정렬
for i in range(n-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:  # 앞 요소가 클 경우
            lst[j], lst[j+1] = lst[j+1], lst[j]  # 뒷 요소와 교환

for n in lst:
    print(n)
