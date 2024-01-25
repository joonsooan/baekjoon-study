import sys
input = sys.stdin.readline

n, k = map(int, input().split())
url_dict = {}

for _ in range(n):
    url, pw = map(str, input().split())
    url_dict[url] = pw

for _ in range(k):
    target_url = input().rstrip()
    print(url_dict[target_url])
