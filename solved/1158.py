# dequeue 풀이
# from collections import deque

# n, k = map(int, input().split())
# deq = deque([i for i in range(1, n + 1)])
# result = []

# while deq:
#     for i in range(k - 1):
#         deq.append(deq.popleft())
#     result.append(str(deq.popleft()))
# print(f"<{', '.join(result)}>")

# stack 풀이
N, K = map(int, input().split())
ans = []
arr = [i for i in range(1, N+1)]
num = 0
for i in range(N):
    num += (K-1)
    if num >= len(arr):
        num %= len(arr)
    ans.append(str(arr[num]))
    arr.pop(num)

print(f"<{', '.join(ans)}>")
