import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 합 s 되는 경우의 수
cnt = 0

for i in range(1, n+1):
    case = combinations(arr, i) # arr에서 i개 뽑기

    for x in case:
        if sum(x) == s:
            cnt += 1


cnt_case = 0

def dfs(num, sum):
    global cnt_case

    if num >= n:
        return
    sum += arr[num]
    if sum == s:
        cnt += 1

    dfs(num+1, sum)
    dfs(num+1, sum - arr[num])

dfs(0, 0)
print(cnt)

cnt = 0
ans = []
def solve(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1
    
    for i in range(start, N):
        ans.append(arr[i])
        solve(i+1)
        ans.pop()

solve(0)
print(cnt)