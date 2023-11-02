import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cost_lst = list(int(input()) for _ in range(n))
start, end = 1, sum(cost_lst)
max_cost = max(cost_lst)
k = max_cost

while start <= end:
    mid = (start + end) // 2
    balance = mid  # First withdrawal
    cnt = 1

    # Counting times of withdrawal
    for cost in cost_lst:
        if balance < cost:  # Can't pay cost with current balance
            balance = mid   # Withdraw mid
            cnt += 1        # Count withdrawal
        balance -= cost

    # Counted more times than m, or mid is smaller than max cost
    if cnt > m or mid < max_cost:  # Must make mid larger
        start = mid + 1

    # Paying with current mid value is possible
    # If cnt equals m -> OK
    # Even if cnt is smaller than m, we can withdraw m times manually
    # We can still find minimum mid value, so 'end = mid - 1'
    else:
        end = mid - 1
        k = mid

print(k)
