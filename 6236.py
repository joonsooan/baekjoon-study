import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cost_lst = []
for _ in range(n):
    cost_lst.append(int(input()))
start, end = 1, 10000*n
k_min = end

while start <= end:
    print()
    print("################")
    print("initialized")
    print("################")
    print(f"start: {start}")
    print(f"end: {end}")
    k = (start + end) // 2
    balance = 0
    count = 0

    # Counting times of withdrawal
    for cost in cost_lst:
        if cost <= balance:
            balance -= cost

        else:
            count += 1
            balance = k
            balance -= cost

    # Deciding whether k is appropriate
    if count < m:
        end = k - 1
    elif count > m:
        start = k + 1
    else:
        start = k + 1
        # There can be various k values that are possible, so find minimum k value
        if k < k_min:
            k_min = k

print(k_min)
